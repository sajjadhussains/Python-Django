from django.shortcuts import render,HttpResponse

def home(request):
    return HttpResponse("""
                        <h1>This is Home Page</h1>
                        <a href="/first_app/course/">contact</a>
                        <a href="/first_app/about/">about</a>
                        <a href="/second_app/course/">course</a>
                        <a href="/second_app/feedback/">feedback</a>
                        """)