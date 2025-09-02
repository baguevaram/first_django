from django.urls import path

from . import views

app_name = "polls"

urlpatterns = [
    path("", views.index, name="index"),
    path("p1", views.p1, name="p1"),
    path('owner', views.owner, name='owner'),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]