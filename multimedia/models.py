# models media
from django.db import models

# Create your models here.
class Photo(models.Model):
  title = models.CharField(max_length=50)
  date_added = models.DateField()
  photographer = models.ForeignKey('contributors.Contributor')
  section = models.ForeignKey('sections.Section', blank=True)
  categories = models.ManyToManyField('sections.Category', blank=True)
  #add link to actual photo