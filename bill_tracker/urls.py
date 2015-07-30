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
import docs.views
# Deprecated
import annotation_app as annote_app


urlpatterns = [
  url(r'^$', docs.views.home, name='home'),
  url(r'^about-us.html/', docs.views.about_us),
  url(r'^contact-us.html/', docs.views.contact_us),
  #url(r'^samplecontact/', docs.views.sample_contact),

  url(r'^bills/', include('annotation_app.routes.bills_routes')),
  # Deprecated
  url(r'^addbill/$', annote_app.controllers.bills_controller.pull_bill),

  url(r'^authors/', include('annotation_app.routes.authors_routes')),
  # Deprecated
  url(r'^get_author_list/$', annote_app.views_deprecated.get_author_list),
  url(r'^get_author_bills/$', annote_app.views_deprecated.get_author_bills),

  url(r'^subjects/', include('annotation_app.routes.subjects_routes')),
  # Deprecated
  url(r'^get_subject_list/$', annote_app.views_deprecated.get_subject_list),
  url(r'^get_subject_bills/$', annote_app.views_deprecated.get_subject_bills),

  url(r'^annotations/', include('annotation_app.routes.annotations_routes')),
  url(r'^docs/', include('docs.urls')),
]
