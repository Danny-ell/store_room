from django.urls import path
from . import views

urlpatterns=[
    path("", views.say_hello),
    path("/Live", views.new_window, name="new_window")
]
