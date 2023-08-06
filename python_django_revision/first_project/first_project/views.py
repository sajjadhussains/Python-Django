from django.http import HttpResponse


def home(request):
    return HttpResponse('This is Home page')

def about(request):
    return HttpResponse('This is About Page')