from django.contrib import admin
from django import forms
from pagedown.widgets import AdminPagedownWidget
from models import AboutDownload,AboutAuthorDetail

class AboutDownloadAdmin(admin.ModelAdmin):
    list_display = ('downloadTitle', 'downloadTime')
    search_fields = ('downloadTitle', 'downloadTime',)
    fieldsets = (
        (
            None,
            {
                'fields': ('downloadTitle', 'downloadHref', 'downloadTime', "downloadNum")
            }
        ),
    )

class AboutAuthorDetailAdmin(admin.ModelAdmin):
    list_display = ('authorDetailDes', 'authorDetailTime')
    search_fields = ('authorDetailDes', 'authorDetailTime', "authorDetailFlag")
    fieldsets = (
        (
            None,
            {
                'fields': ('authorDetailDes', 'authorDetailTime', 'authorDetailFlag', 'authorDetailHref')
            }
        ),
    )

admin.site.register(AboutDownload, AboutDownloadAdmin)
admin.site.register(AboutAuthorDetail, AboutAuthorDetailAdmin)
