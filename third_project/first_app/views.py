from django.shortcuts import render

# Create your views here.

def contact(request):
    return render(request,'./first_app/index.html',context={'author':'sajjad','age':17,'cgpa':2.8})
