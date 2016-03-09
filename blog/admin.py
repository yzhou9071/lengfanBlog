from django.contrib import admin
from django import forms
from pagedown.widgets import AdminPagedownWidget
from models import Category, Article

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', )
    search_fields = ('title', )
    fieldsets = (
        (
            None,
            {
                'fields': ('categoryID', 'title', 'slug',)
            }
        ),
    )

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        widgets = {
            'content_markdown' : AdminPagedownWidget(),
        }
        exclude = ['content_markup',]

class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'publishTime')
    search_fields = ('title', 'content_markdown',)
    list_filter = ('categories',)
    fieldsets = (
        (
            None,
            {
                'fields': ('title', 'slug', 'tags', 'content_markdown', 'categories', 'pv',)
            }
        ),
    )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
