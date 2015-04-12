# admin articles
from django.contrib import admin
from django.db import models
from django import forms

from articles.models import Article

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    date_hierarchy = 'publish_date'
    list_display = ('title', 'get_authors', 'section', 'main_category', 'publish_date', 'ready')
    list_filter = ['publish_date', 'section', 'main_category']
    filter_horizontal = ['authors', 'categories']
    list_per_page = 19
    list_editable = ['ready', 'publish_date']
    search_fields = ('title', 'categories', 'main_category', 'content')

    formfield_overrides = {models.TextField: {'widget': forms.Textarea(attrs={'class': 'ckeditor'})}, }

    class Media:
        js = ('ckeditor/ckeditor.js',)


admin.site.register(Article, ArticleAdmin)
