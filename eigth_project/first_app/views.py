from django.shortcuts import render
from first_app.models import Teacher,Student
# Create your views here.

def home(request):
    return render(request,'home.html')

def show_data(request):
    # teacher = Teacher.objects.get(name='Bakar')
    # students = teacher.student.all()
    # for stud in students:
    #     print(stud.name)
    
    student = Student.objects.get(name = 'sajjad')
    # teachers = student.teacher_set.all()
    teachers = student.teachers.all()
    for teacher in teachers:
        print(f"{teacher.name} {teacher.subject} {teacher.mobiles}")
    return render(request,'show_data.html')

