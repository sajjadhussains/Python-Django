from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('first_app/',views.show_data)
]
