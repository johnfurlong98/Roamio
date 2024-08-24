from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import destination
from django.contrib.auth.decorators import login_required
from .forms import DestinationForm

# View to list all active destinations
def destination_list(request):
    destinations = destination.objects.filter(status=1).order_by('-created_on')
    return render(request, 'destinations/destination_list.html', {'destinations': destinations})

# View to show details of a specific destination
def destination_detail(request, pk):
    destination = get_object_or_404(destination, pk=pk)
    return render(request, 'destinations/destination_detail.html', {'destination': destination})

# View to handle creation of a new destination, only accessible by logged-in users
@login_required
def destination_create(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            destination = form.save(commit=False)
            destination.author = request.user
            destination.save()
            return redirect('destination_detail', pk=destination.pk)
    else:
        form = DestinationForm()
    return render(request, 'destinations/destination_form.html', {'form': form})

# Index view (could be your home page or a landing page)
def index(request):
    return render(request, 'index.html')
