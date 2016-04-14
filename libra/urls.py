"""libra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from myweblab import settings

from libra.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^search/$', search, name="search"),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^index/$', TemplateView.as_view(template_name="index.html")),
    url(r'^mobsearch/$', TemplateView.as_view(template_name="mobsearch.html")),
    url(r'^help/$', TemplateView.as_view(template_name="help.html")),
    url(r'^deals/$', deals, name="deals"),
    url(r'^compare/(?P<prodid>.*)$', compare, name="compare"),
    url(r'^search/sort/(?P<method>.*)$', sort, name="sort"),
    url(r'^search/filter/$', filterr, name="filter"),
    url(r'^search/filter/sort_filtered/(?P<method>.*)$', sort_filtered, name="sort_filtered"),
    url(r'^flip_delivery$', flip_delivery, name="flip_delivery"),
    url(r'^amazon_delivery$', amazon_delivery, name="amazon_delivery"),
    url(r'^snapdeal_delivery$', snapdeal_delivery, name="snapdeal_delivery"),
    url(r'^ebay_delivery$', ebay_delivery, name="ebay_delivery"),
]

<<<<<<< HEAD
urlpatterns += staticfiles_urlpatterns()
=======
# urlpatterns += staticfiles_urlpatterns()
>>>>>>> 03d8735c63341c45ae9dc662155abeb92afd5cdb

# urlpatterns += patterns('',
#     url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
# )
