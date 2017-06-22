from django.conf.urls import url
from contentParser import views


urlpatterns = urlpatterns = [
    url(r'^$', views.parse_content),
]