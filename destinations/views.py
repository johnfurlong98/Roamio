from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from .models import Destination, Comment, UserCommentLikes, UserDestinationLikes
from django.contrib.auth.decorators import login_required
from .forms import DestinationForm, CommentForm
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import DestinationSerializer, CommentSerializer
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.decorators import action
from rest_framework import status
from django.conf import settings


class DestinationViewset(viewsets.ModelViewSet):

    serializer_class = DestinationSerializer
    queryset = Destination.objects.none()

    def get_queryset(self, request):
        id = request.query_params.get("id", None)
        queryset = Destination.objects.all()
        if id:
            queryset = queryset.filter(id=id)

        data = DestinationSerializer(queryset, many=True).data

        return Response(data)

    def create(self, request):
        try:
            name = request.data["name"]
            location = request.data["location"]
            email = request.data["email"]
            description = request.data["description"]

        except Exception as e:
            print(e)
            return HttpResponse("Missing Data")

        created_on = request.data.get("created_on", timezone.now())
        status = request.data.get("status", 1)

        try:
            user = User.objects.get(email=email)
        except:
            return HttpResponse("Missing User")
        try:
            new_destination = Destination.objects.get(name=name)
            return HttpResponse("Destination already exists")
        except:
            new_destination = Destination.objects.create(
                name=name,
                location=location,
                author=user,
                created_on=created_on,
                description=description,
                status=status,
            )
        data = DestinationSerializer(new_destination).data

        return Response(data)

    def partial_update(self, request, id):
        try:
            destination = Destination.objects.get(id=id)
            print(vars(request))
            print(destination)
            user = request._user.id

            if UserDestinationLikes.objects.filter(
                user=user, destination=destination
            ).exists():
                return HttpResponse("Already Liked")
        except Exception as e:
            print(e)
            return HttpResponse({"Missing Data"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            destination.likes += 1
            destination.save()
            serialized_data = DestinationSerializer(destination).data
            return Response(serialized_data)
        except:
            return HttpResponse("Error liking comment")

    def delete(self, request, id):
        if not id:
            return HttpResponse("No id provided")

        try:
            destination = Destination.objects.get(id=id)
        except:
            return HttpResponse("Destination does not exist")

        destination.delete()
        return HttpResponse("Destination Deleted")


class DestinationTemplates(viewsets.ViewSet):

    @action(detail=False, methods=["get"])
    def get_destination_list(self, request):
        destinations = Destination.objects.all()
        data = DestinationSerializer(destinations, many=True).data
        return render(
            request, "destinations/destination_list.html", {"destinations": data}
        )

    @action(detail=False, methods=["get", "post"])
    def get_destination_detail(self, request, id):
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                user = User.objects.get(id=request._user.id)
                destination = Destination.objects.get(id=id)
                Comment.objects.create(
                    user=user, text=form.cleaned_data["text"], destination=destination
                )
                # url = reverse('destination-detail')
                url = "destination-detail"
                return redirect(url, id=id)

        destination = Destination.objects.get(id=id)
        data = DestinationSerializer(destination).data
        comments = Comment.objects.filter(destination=id)
        comment_data = CommentSerializer(comments, many=True).data
        form = CommentForm
        return render(
            request,
            "destinations/destination_detail.html",
            {
                "destination": data,
                "cloud_name": settings.CLOUDINARY_CLOUD_NAME,
                "form": form,
                "comments": comment_data,
            },
        )

    @action(detail=False, methods=["get"])
    def get_destination_form(self, request):
        if request.method == "POST":
            form = DestinationForm(request.POST)
            if form.is_valid():
                user = User.objects.get(id=request._user.id)
                Destination.objects.create(
                    name=form.cleaned_data["name"],
                    location=form.cleaned_data["location"],
                    description=form.cleaned_data["description"],
                    featured_image=form.cleaned_data["image"],
                    author=user,
                )

                url = reverse("destinations-list")
                return redirect(url)

            else:
                return HttpResponse("Invalid Form")
        else:
            form = DestinationForm()
            return render(
                request,
                "destinations/destination_form.html",
                {"form": form, "destination": "destination_list"},
            )


class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all()

    def get_queryset(self, request):
        destination = request.query_params.get("destination", None)
        user = request.query_params.get("user", None)

        queryset = Comment.objects.all()

        if destination:
            queryset = queryset.filter(destination=destination)

        if user:
            queryset = queryset.filter(user=user)

        serialized_data = CommentSerializer(queryset, many=True)
        return Response(serialized_data)

    def create(self, request):
        try:
            destination = request.data["destination"]
            user = request.data["user"]
        except Exception as e:
            return HttpResponse("Missing Data")

        try:
            text = request.data["text"]
        except:
            return HttpResponse("Comment cant be empty!")

        comment = Comment.objects.create(destination=destination, user=user, text=text)
        serialized_data = CommentSerializer(comment).data

        return Response(serialized_data)

    def partial_update(self, request, id):
        try:
            comment = Comment.objects.get(id=id)
            user = request._user.id
            if UserCommentLikes.objects.filter(user=user, comment=comment).exists():
                return HttpResponse("Already Liked")
        except:
            return HttpResponse("Missing Data")
        try:
            comment.likes = comment.likes + 1
            comment.save()
            serialized_data = CommentSerializer(comment).data
            return Response(serialized_data)
        except:
            return HttpResponse("Error liking comment")

    def delete(self, request, id):
        if not id:
            return HttpResponse("No id provided")

        try:
            comment = Comment.objects.get(id=id)
        except:
            return HttpResponse("Destination does not exist")

        comment.delete()
        return HttpResponse("Destination Deleted")
