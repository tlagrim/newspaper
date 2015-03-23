from django.contrib import admin

from featured.models import MainStory, FeaturedArticle


# Register your models here.
admin.site.register(MainStory)
admin.site.register(FeaturedArticle)