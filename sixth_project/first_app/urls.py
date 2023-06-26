from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home,name="homepage"),
    path('delete/<int:rools>',views.delete_student,name="delete_student")
]
