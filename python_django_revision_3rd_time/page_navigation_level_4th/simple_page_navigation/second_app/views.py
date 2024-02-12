from django.shortcuts import render,HttpResponse

# Create your views here.

def course(request):
        return HttpResponse("""
                        <h1>This is Course page</h1>
                        <a href="/">home</a>
                        <a href="/first_app/about/">contact</a>
                        <a href="/first_app/about/">about</a>
                        <a href="/second_app/feedback/">feedback</a>
                        """)

def feedback(request):
    return HttpResponse("""
                        <h1>This is Feedback page</h1>
                        <a href="/">home</a>
                        <a href="/first_app/about/">About</a>
                        <a href="/second_app/course/">Course</a>
                        <a href="/second_app/feedback/">feedback</a>
                        """)