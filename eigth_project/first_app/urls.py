from django.urls import path
from first_app.views import home,show_data

urlpatterns = [
    path('',home),
    path('show_data/',show_data)
]
