from django.shortcuts import render,redirect
from . import models
# Create your views here.

def home(request):
    data = models.Student.objects.all()
    # print(data)
    return render(request,"home.html",{'data':data})

def delete_student(request,rools):
    std = models.Student.objects.get(pk=rools).delete()
    student = models.Student.objects.all()
    return redirect("homepage")
    
