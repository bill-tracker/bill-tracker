from django.conf.urls import url
from annotation_app.controllers import bills_controller
# Deprecated
from annotation_app import views_deprecated


### Bills routes
# bills routes to controller actions below.
# bills handles the bill_list and adding bills

def bills(request):
  if request.method == 'GET':
    return views_deprecated.bill_list(request)

  elif request.method == 'POST':
    return bills_controller.create(request)


### Bills URLs
urlpatterns = [

  url(r'^$', bills, name='bills'),
  url(r'^get-bill-info/$', bills_controller.get_bill_info,
    name='get_bill_info'),
  # Deprecated
  url(r'^(?P<bill_id>\d+)/$', bills_controller.redirect_get_one, name='bill'),
  url(r'^(?P<bill_slug>[SHsh][Bb]\d+)/$', bills_controller.get_one,
    name='bill_by_slug'),

  # Deprecated
  url(r'^addbill/$', bills_controller.pull_bill, name='add_bill'),
]
