# main urls
from django.conf.urls import patterns, include, url
from django.contrib import admin

import homepage.views
import sections.views
import newspaper.views
from django.views.generic import TemplateView

#this should replace the password reset URL code, all URLs will automatically be referenced by django
urlpatterns = [
    url('^', include('django.contrib.auth.urls'))
]

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'newspaper.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^$', homepage.views.homepage),
                       # url(r'^categories/(?P<category_url>[\w-]+)', sections.views.category_page, name='category_page'),
                       #add year to article url
                       #password reset URL Syntax blow
                       #url(r'^reset/password_reset/$', 'django.contrib.auth.views.password_reset', name='reset_password_reset1'),
                       #url(r'^reset/password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
                       #url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
                       #url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
                       #end password reset URL
                       url(r'^admin', include(admin.site.urls)),
                       url(r'^articles/', include('articles.urls')),
                       url(r'^contributors/', include('contributors.urls')),
                       url(r'^contact', newspaper.views.about_page),
                       url(r'^advertise', TemplateView.as_view(template_name="advertise.html")),
                       url(r'^about', newspaper.views.about_page),
                       url(r'^(?P<section_url>[\w-]+)', sections.views.section_page, name='section_page'),
                       #hardcode sections into here
                       )
