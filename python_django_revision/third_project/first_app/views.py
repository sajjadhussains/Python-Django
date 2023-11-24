from django.shortcuts import render

# Create your views here.

def contact(request):
    return render(request,'first_app/index.html',{'name':'phitron','age':17,'marks':88,
                                                  'courses':[
                                                      {
                                                        'id':1,
                                                        'course_name':'C',
                                                        'teacher':'Rahim'
                                                      },
                                                      {
                                                          'id':2,
                                                          'course_name':'Python',
                                                          'teacher':'Bakar'
                                                      },
                                                      {
                                                          'id':3,
                                                          'course_name':'javascript',
                                                          'teacher':'Karim'
                                                      }
                                                  ],
                                                  'blog':'amar shonar bangla ami tomai valobashi,jonmo diyeso ma go tai,tomai valobashi'})
