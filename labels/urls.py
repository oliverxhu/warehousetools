from django.conf.urls import url
from . import views # from the current folder import views.py

app_name = 'labels'
urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^(?P<barcode>.*)/(?P<pallet_number>.*)/(?P<sku>.*)/(?P<supplier>.*)/$', views.label, name='label'),

]