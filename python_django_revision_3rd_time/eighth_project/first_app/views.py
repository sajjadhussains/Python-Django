from django.shortcuts import render
from first_app.forms import StudentForm
from first_app.models import StudentModel
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