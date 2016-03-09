from django.contrib import admin
from django import forms
from pagedown.widgets import AdminPagedownWidget
from models import PhotoList

# Register your models here.
class PhotoListAdmin(admin.ModelAdmin):
    list_display = ('photoTitle', )
    search_fields = ('photoTitle', 'photoDes',)
    fieldsets = (
        (
            None,
            {
                'fields': ('photoTitle', 'photoDes',)
            }
        ),
    )
admin.site.register(PhotoList, PhotoListAdmin)
