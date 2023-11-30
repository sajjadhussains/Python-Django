from django.shortcuts import render
from . forms import StudentData
# Create your views here.

def home(request):
    return render(request,'./first_app/index.html',{'author':'Sajjad','age':19,'mark':89,'friends':[
        {
            'id':1,
            'name':'Bilas',
            'persepective':'was good but not trusted'
        },
        {
            'id':2,
            'name':'Miad',
            'persepective':'not matured'
        },
        {
            'id':3,
            'name':'Shanto',
            'persepective':'trusted'
        }
    ]})

def about(request):
    if request.method == 'POST':
        name=request.POST.get('username')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request,'./first_app/about.html',{'name':name,'email':email,'select':select})
    else:
        return render(request,'./first_app/about.html')
def submit_form(request):
        return render(request,'./first_app/form.html')
    
def DjangoForm(request):
    form = StudentData(request.POST)
    if form.is_valid():
        print(form.cleaned_data);
    return render(request,'./first_app/django_form.html',{'form':form})
    