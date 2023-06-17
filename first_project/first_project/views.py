from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, This is my first Django web page")

def about(request):
    return HttpResponse("This is About Page")