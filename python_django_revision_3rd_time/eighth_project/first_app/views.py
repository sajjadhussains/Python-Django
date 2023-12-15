from django.shortcuts import render
from first_app.forms import StudentForm
from first_app.models import StudentModel,Teacher,Student
# Create your views here.

def home(request):
    form = StudentForm(request.POST)
    students = StudentModel.objects.all();
    if form.is_valid():
        form.save()
        print(form.cleaned_data)
    else:
        form = StudentForm()
    return render(request,'home.html',{'form':form,'students':students})

def show_data(request):
    #all students list of individual teacher
    # teacher = Teacher.objects.get(name="Mahabub")
    # student = teacher.student.all()
    # for std in student:
    #     print(std.name)
    #teachers for individual student
    student = Student.objects.get(name='nahid')
    teachers = student.teachers.all()
    for teacher in teachers:
        print(teacher.name)
    return render(request,'data.html')