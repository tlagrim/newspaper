# admin articles
from django.contrib import admin
from django.db import models
from django import forms

from articles.models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_published'
    list_display = ('title', 'section', 'main_category', 'date_published', 'ready')
    list_filter = ['date_published', 'section', 'main_category']
    filter_horizontal = ['authors', 'categories']
    formfield_overrides = {models.TextField: {'widget': forms.Textarea(attrs={'class': 'ckeditor'})}, }
    class Media:
        js = ('ckeditor/ckeditor.js',)


admin.site.register(Article, ArticleAdmin)
