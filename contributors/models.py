#contributors models
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
	middle_name = models.CharField(max_length=50,blank=True)
	last_name = models.CharField(max_length=50)
	suffix = models.CharField(max_length=5)
	twitter = models.SlugField(db_index=True)
	email = models.EmailField(max_length=75)
	bio = models.TextField()
	description = models.CharField(max_length=200)
	#roll/editor
	#picture (1)
	class_standing = models.CharField(max_length=2, choices=CLASS_STANDING_OPTIONS,blank=True)
	def __str__(self):
		return self.first_name + ' ' + self.last_name