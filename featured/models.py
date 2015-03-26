# models featured
from django.db import models

# Main stories are the articles (stories) which appear in the Flexslider on the homepage
class MainStory(models.Model):
    article = models.ForeignKey('articles.Article', related_name='+')
    # order field is a bad hack to properly order the articles. This way, editors can choose the order the articles
    # appear in. TODO: look into django-admin-orderable (something like that)
    order = models.IntegerField()
    def __str__(self):
        return "Main Story number " + str(self.order)
    class Meta:
        ordering = ['order']
        verbose_name_plural = 'Main stories'

# Featured articles are the article from each section which appear either at the top of the section page or
# in the sections display on the homepage. There should only ever be one instance of this model for each section.
# TODO: look into the Django models.clean() method for enforcing only one instance of this model
# TODO: (ie) http://stackoverflow.com/questions/2138408/limit-number-of-model-instances-to-be-created-django
class FeaturedArticle(models.Model):
    article = models.ForeignKey('articles.Article', related_name='+')
    section = models.ForeignKey('sections.Section')
    def __str__(self):
        return self.section.name + " Featured Article"

# # PinnedArticles is plural because there will only be one instance of this model
# # and it will contain all of the pinned articles
# # PinnedArticles keeps track of the articles which appear in slide show on the homepage
# class PinnedArticles(models.Model):
#     firstPinnedArticle = models.ForeignKey('articles.Article', related_name='+')
#     secondPinnedArticle = models.ForeignKey('articles.Article', related_name='+')
#     thirdPinnedArticle = models.ForeignKey('articles.Article', related_name='+')
#     forthPinnedArticle = models.ForeignKey('articles.Article', related_name='+')
#     fifthPinnedArticle = models.ForeignKey('articles.Article', related_name='+')
#
#
# # FeaturedArticle keeps track of the featured article in each section.
# # These are the articles which appear at the top of the section page, as well as on the home page
# # There should only be one instance of this model for each section
# class FeaturedArticle(models.Model):
#     section = models.ForeignKey('sections.Section')
#     article = models.ForeignKey('articles.Article')
