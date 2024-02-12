from django.shortcuts import render,HttpResponse

# Create your views here.

def contact(request):
    return HttpResponse("""
                        <h1>This is Contact page</h1>
                        <a href="/first_app/about/">About</a>
                        <a href="/second_app/course/">Course</a>
                        <a href="/second_app/feedback/">feedback</a>
                        """)

def about(request):
     return HttpResponse("""
                        <h1>This is About page</h1>
                        <a href="/first_app/contact/">Contact</a>
                        <a href="/second_app/course/">Course</a>
                        <a href="/second_app/feedback/">feedback</a>
                        """)