from django.contrib import admin

from featured.models import PinnedArticles, FeaturedArticle


# Register your models here.
admin.site.register(PinnedArticles)
admin.site.register(FeaturedArticle)