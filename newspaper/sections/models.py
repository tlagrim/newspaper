# models sections
from django.db import models

# Create your models here.
class Section(models.Model):
    name = models.CharField(max_length=20)
    url = models.SlugField(db_index=True)


    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(max_length=20)
    url = models.SlugField(db_index=True)
    section = models.ForeignKey('Section', null=True, blank=True)

    def __str__(self):
        return self.name