"""URL configuration for the movies app."""

from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path("",  view=views.index, name="index"),
    path("<int:movie_id>",  view=views.detail, name="detail")
]
