# models featured
from django.db import models


# PinnedArticles is plural because there will only be one instance of this model
# and it will contain all of the pinned articles
# TODO: look into the Django models.clean() method for enforcing only one instance of this model
# TODO: (ie) http://stackoverflow.com/questions/2138408/limit-number-of-model-instances-to-be-created-django
# PinnedArticles keeps track of the articles which appear in slide show on the homepage
class PinnedArticles(models.Model):
    firstPinnedArticle = models.ForeignKey('articles.Article', related_name='+')
    secondPinnedArticle = models.ForeignKey('articles.Article', related_name='+')
    thirdPinnedArticle = models.ForeignKey('articles.Article', related_name='+')
    forthPinnedArticle = models.ForeignKey('articles.Article', related_name='+')
    fifthPinnedArticle = models.ForeignKey('articles.Article', related_name='+')


# FeaturedArticle keeps track of the featured article in each section.
# These are the articles which appear at the top of the section page, as well as on the home page
# There should only be one instance of this model for each section
class FeaturedArticle(models.Model):
    section = models.ForeignKey('sections.Section')
    article = models.ForeignKey('articles.Article')
