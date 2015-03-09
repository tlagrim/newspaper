# contributor urls
from django.conf.urls import patterns, url

from contributors import views

urlpatterns = patterns('',
                       url(r'(?P<contributor_url>[\w-]+)', views.contributor_page),
)