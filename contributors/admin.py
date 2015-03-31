# contributer admin
from django.contrib import admin
from django.db import models
from contributors.models import Contributor, Position

# Register your models here.


class ContributorAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'position', 'twitter', 'email', 'class_standing')
    list_filter = ('position', 'class_standing')
    list_per_page = 19

admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Position)
