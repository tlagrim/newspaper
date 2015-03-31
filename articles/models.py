# Articles models
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=50)
    url = models.SlugField(db_index=True)
    image = models.URLField() 
    content = models.TextField(verbose_name='')
    ready = models.BooleanField(default=False)
    preview = models.CharField(max_length=200)
    publish_date = models.DateField()
    authors = models.ManyToManyField('contributors.Contributor')
    section = models.ForeignKey('sections.Section')
    main_category = models.ForeignKey('sections.Category', related_name='+')
    categories = models.ManyToManyField('sections.Category', blank=True)

    def __str__(self):
        return self.title

    def get_authors(self):
        a = ''
        for author in self.authors.all():
            a += author.__str__() + ', '
        return a[:-2]

    def get_absolute_url(self):
        return "/articles/" + self.url