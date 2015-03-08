#Admin sections
from django.contrib import admin
from sections.models import Section, Category
# Register your models here.

admin.site.register(Section)
admin.site.register(Category)