from django.contrib import admin
from .models import Destination  

# Register your models here.
admin.site.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'author', 'status', 'created_on')
    list_filter = ('status', 'created_on', 'author')
    search_fields = ('name', 'location', 'description')
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'created_on'
    ordering = ('status', 'created_on')