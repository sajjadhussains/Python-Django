from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def department(request):
    return HttpResponse('''
                        <h1>This is Department Page</h1>
                        <a href="">Home</a>
                        <a href="/student/about/">About</a>
                        <a href="/student/courses/">Courses</a>
                        <a href="/teacher/faculty/">Faculty</a>
                        ''')
    
def faculty(request):
    return HttpResponse('''
                        <h1>This is Faculty Page</h1>
                        <a href="">Home</a>
                        <a href="/student/about/">About</a>
                        <a href="/student/courses/">Courses</a>
                        <a href="/teacher/department">Department</a>
                        ''')