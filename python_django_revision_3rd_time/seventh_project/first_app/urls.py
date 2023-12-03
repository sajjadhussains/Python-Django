from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="homepage"),
    path('delete/<int:roll>',views.delete_std,name="delete_student")
]
