from django.shortcuts import render

# Create your views here.

def contact(request):
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