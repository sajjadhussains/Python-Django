from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def contact(request):
    return HttpResponse(
    """
    <h1>this is contact Page</h1>
    <a href='/second_app/courses/'>courses</a>
    <a href='/second_app/feedback/'>feedback</a>
    <a href='/first_app/about/'>About</a>
    """
    )
def about(request):
    return HttpResponse(
         """
    <h1>this is about Page</h1>
    <a href='/second_app/courses/'>courses</a>
    <a href='/second_app/feedback/'>feedback</a>
    <a href='/first_app/contact/'>Contact</a>
    """
    )