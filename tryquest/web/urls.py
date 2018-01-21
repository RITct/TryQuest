from django.conf.urls import url, include
from tryquest.web import views


urlpatterns = [
    url(r'^$', views.index, name="index"),
]
