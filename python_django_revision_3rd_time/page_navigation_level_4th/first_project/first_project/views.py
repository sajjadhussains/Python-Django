from django.shortcuts import render,HttpResponse

def home(request):
    return HttpResponse("<h1>This is Home page</h1>");