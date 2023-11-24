from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>I am Sajjad</h1>');

def about(request):
    return HttpResponse('<h2>I am learning Python Django</h2>');