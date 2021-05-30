from django.urls import path
from . import views


app_name = 'psycho_tests'
urlpatterns = [
    path("poll/", views.poll, name="poll"),
    path("verdict/", views.verdict, name="verdict"),
    path("", views.index, name="index")
]