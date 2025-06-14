from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("p1", views.p1, name="p1"),
]