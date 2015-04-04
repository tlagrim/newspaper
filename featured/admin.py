from django.contrib import admin

from featured.models import MainStory, FeaturedArticle, PinnedArticle


class MainStoryAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'article')
    list_editable = ['article']


class FeaturedArticleAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'article')
    list_editable = ['article']


class PinnedArticleAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'article')
    list_editable = ['article']

# Register your models here.
admin.site.register(MainStory, MainStoryAdmin)
admin.site.register(FeaturedArticle, FeaturedArticleAdmin)
admin.site.register(PinnedArticle, PinnedArticleAdmin)