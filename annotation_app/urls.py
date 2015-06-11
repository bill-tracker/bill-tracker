"""bill_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from annotation_app import views

urlpatterns = [
<<<<<<< HEAD
    #url(r'^index/$', views.index),
    url(r'^$', views.bill_list, name='bill_list'),#shows list of bills current homepage
    url(r'^bills/$', views.bill_list, name='bills'),#same as bill list/root
    url(r'^addbill/$', views.add_bill, name='add_bill'),#allows user to add bill. 
    url(r'^bills/(?P<bill_id>\d+)/$', views.bill, name='bill'), #shows a specific bill
    url(r'^bills/(?P<bill_id>\d+)/edit/$', views.edit_bill, name='edit_bill'),#allows us to edit it.
    #url(r'^addannotation/$', views.add_annotation, name='add_annotation'),
    #url(r'^annotations/(?P<annotation_id>\d+)/$', views.annotation,
    #  name='annotation'),
    #url(r'^addcomment/$', views.add_comment, name='add_comment'),
    #url(r'^comments/(?P<comment_id>\d+)/$', views.comment, name='comment'),
    url(r'^example-client/$', views.example_client, name='example_client'), #shows how to use the json
    url(r'^getbill/$', views.get_bill, name='get_bill'), #gives json version of the bill 
    url(r'^megalith/$', views.megalith, name='megalith'), #TODO fold this into annotations
=======
    url(r'^index/$', views.index),
    url(r'^$', views.bill_list, name='bill_list'),
    url(r'^bills/$', views.bill_list, name='bills'),
    url(r'^addbill/$', views.add_bill, name='add_bill'),
    url(r'^bills/(?P<bill_id>\d+)/$', views.bill, name='bill'),
    url(r'^bills/(?P<bill_id>\d+)/edit/$', views.edit_bill, name='edit_bill'),
    url(r'^addannotation/$', views.add_annotation, name='add_annotation'),
    url(r'^annotations/(?P<annotation_id>\d+)/$', views.annotation,
      name='annotation'),
    url(r'^addcomment/$', views.add_comment, name='add_comment'),
    url(r'^comments/(?P<comment_id>\d+)/$', views.comment, name='comment'),
    url(r'^example-client/$', views.example_client, name='example_client'),
    url(r'^megalith/$', views.megalith, name='megalith'),
>>>>>>> 893d7ffba90ef59026d0713c7da0220267151fe1
]
