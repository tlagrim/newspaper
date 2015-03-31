from django.contrib import admin
from django.db import models

from featured.models import MainStory, FeaturedArticle


class MainStoryAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'article')
    list_editable = ['article']


class FeaturedArticleAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'article')
    list_editable = ['article']

# Register your models here.
admin.site.register(MainStory, MainStoryAdmin)
admin.site.register(FeaturedArticle, FeaturedArticleAdmin)