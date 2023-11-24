from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def about(request):
    return HttpResponse('''
                        <h1>This is about Page</h1>
                        <a href="/student/courses/">Courses</a>
                        <a href="/teacher/department/">Department</a>
                        <a href="/teacher/faculty/">Faculty</a>
                        ''')
def courses(request):
    return HttpResponse('''
                        <h1>This is Courses Page</h1>
                        # <a href="">Home</a>
                        <a href="/student/about/">About</a>
                        <a href="/teacher/department/">Department</a>
                        <a href="/teacher/faculty/">Faculty</a>
                        ''')