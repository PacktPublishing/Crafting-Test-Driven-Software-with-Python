from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^get$', views.get),
    re_path(r"^anything.*$", views.get),
    re_path(r'^$', views.home)
]