from django.contrib import admin
from .models import Destination, Comment, UserCommentLikes, UserDestinationLikes


# Register your models here.
class DestinationAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "author", "status", "created_on")
    list_filter = ("status", "created_on", "author")
    search_fields = ("name", "location", "description")
    prepopulated_fields = {"slug": ("name",)}
    raw_id_fields = ("author",)
    date_hierarchy = "created_on"
    ordering = ("status", "created_on")


admin.site.register(Destination)

admin.site.register(Comment)

admin.site.register(UserCommentLikes)
admin.site.register(UserDestinationLikes)
