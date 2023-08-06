from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def courses(request):
    return HttpResponse(
         """
    <h1>this is Courses Page</h1>
    <a href='/first_app/about/'>about</a>
    <a href='/first_app/contact/'>contact</a>
    <a href='/second_app/feedback/'>Feedback</a>
    """
    )
def feedback(request):
    return HttpResponse(
         """
    <h1>this is Feedback Page</h1>
    <a href='/first_app/about/'>about</a>
    <a href='/first_app/contact/'>contact</a>
    <a href='/second_app/courses/'>About</a>
    """
    )
