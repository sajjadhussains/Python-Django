from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("courses/",views.courses),
    path("feedback/",views.feedback),
]
