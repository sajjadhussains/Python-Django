from django.http import HttpResponse

def home(request):
    return HttpResponse('''
                        <h1>This is Home Page</h1>
                        <a href="">Home</a>
                        <a href="student/about/">About</a>
                        <a href="student/courses/">Courses</a>
                        <a href="teacher/department">Department</a>
                        <a href="teacher/faculty/">Faculty</a>
                        ''')