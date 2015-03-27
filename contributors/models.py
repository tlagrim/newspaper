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
    POSITIONS = (
        ('N/A', 'N/A'),
        ('peic', 'Print Editor-in-Chief'),
        ('oeic', 'Online Editor-in-Chief'),
        ('news', 'News Editor'),
        ('view', 'Viewpoints Editor'),
        ('life', 'Life & Arts Editor'),
        ('sports', 'Sports Editor'),
        ('dc', 'Design Chief'),
        ('d', 'Designer'),
        ('ope', 'Online Photo Editor'),
        ('pe', 'Photo Editor'),
        ('cc', 'Copy Chief'),
        ('ce', 'Copy Editor'),
        ('abm', 'Advertising & Business Manager'),
        ('w', 'writer'),
        ('p', 'photographer'),
        ('pro','programmer'),
        ('fa', 'Faculty Adviser'),
    )
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    suffix = models.CharField(max_length=5)
    image = models.URLField() 
    twitter = models.SlugField(db_index=True)
    email = models.EmailField(max_length=75)
    bio = models.TextField()
    staff = models.BooleanField(default=False)
    position = models.CharField(max_length=10, choices=POSITIONS, default='N/A')
    description = models.CharField(max_length=200)
    class_standing = models.CharField(max_length=5, choices=CLASS_STANDING_OPTIONS, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

