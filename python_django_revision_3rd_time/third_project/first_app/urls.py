from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='homepage'),
    path('about/',views.about,name='about'),
    path('form/',views.submit_form,name='formpage'),
    path('django_form/',views.DjangoForm,name='django_form')
]
