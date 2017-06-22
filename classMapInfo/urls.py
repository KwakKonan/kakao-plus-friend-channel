from django.conf.urls import url
from classMapInfo import views


urlpatterns = [
    url(r'^$', views.class_map_info_list),
    url(r'^(?P<className>[0-9]+)/$', views.class_map_info_detail),
]