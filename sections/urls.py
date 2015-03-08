#Section URLs
from django.conf.urls import patterns, url

from sections import views

urlpatterns = patterns('',
	url(r'^(?P<section_url>[\w-]+)', views.section_page, name='section_page'),
    url(r'^categories/(?P<category_url>[\w-]+)', views.category_page, name='category_page'),
)