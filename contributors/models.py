# contributors models
from django.db import models


class Contributor(models.Model):
    CLASS_STANDING_OPTIONS = (
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('GR', 'Graduate'),
    )
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    suffix = models.CharField(max_length=5)
    image = models.URLField() 
    twitter = models.SlugField(db_index=True)
    email = models.EmailField(max_length=75)
    bio = models.TextField()
    position = models.ForeignKey('Position')
    description = models.CharField(max_length=200)
    class_standing = models.CharField(max_length=5, choices=CLASS_STANDING_OPTIONS, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Position(models.Model):
    title = models.CharField(max_length=50)
    show_on_about_page = models.BooleanField(default=False)

    def __str__(self):
        return self.title