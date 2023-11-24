from django.shortcuts import render

def home(request):
    return render(request,'./first_app/index.html',{'name':'rahim','marks':86,"courses":[
        {
            "id":1,
            "course":"C",
            "teacher":"Rahim"
        },
        {
            "id":2,
            "course":"C++",
            "teacher":"Karim"
        },
         {
            "id":3,
            "course":"java",
            "teacher":"jabbar"
        }
    ]})

def about(request):
    return render(request,'./first_app/about.html')