#admin articles
from django.contrib import admin
from django.db import models
from articles.models import Article
from django import forms
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
	formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }
	class Media:
		js = ('ckeditor/ckeditor.js',)

admin.site.register(Article,ArticleAdmin)
