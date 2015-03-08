from django.conf.urls import patterns, url

from articles import views

urlpatterns = patterns('',
    url(r'(?P<article_url>[\w-]+)', views.article_page),
)