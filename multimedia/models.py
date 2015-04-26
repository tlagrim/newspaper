# models media
from django.db import models

# Create your models here.
class Photo(models.Model):
    title = models.CharField(max_length=50)
    date_added = models.DateField()
    photographer = models.ForeignKey('contributors.Contributor')
    section = models.ForeignKey('sections.Section', null=True, blank=True)
    categories = models.ManyToManyField('sections.Category', blank=True)
    image = models.FileField(upload_to='photos/%Y/%m/%d')
    # things to do for production
    # define a way to locate image from the URL in the database (thus allowing the author to be determined)
    # add verification to the upload (make sure it is a valid image)

    def __str__(self):
        return self.title