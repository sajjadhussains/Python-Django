from django.contrib import admin
from first_app.models import StudentModel,StudentInfoModel,TeacherInfoModel,EmployeeModel,ManagerModel,Person,Passport,Post
# Register your models here.

admin.site.register(StudentModel)

@admin.register(StudentInfoModel)
class StudentInfoModel(admin.ModelAdmin):
    list_display=["name","city","roll","payment","section"]
    
@admin.register(TeacherInfoModel)
class TeacherInfoModel(admin.ModelAdmin):
    list_display=["name","city","salary"]

@admin.register(EmployeeModel)
class EmployeeModel(admin.ModelAdmin):
    list_display=["id","name","city","designation"]

@admin.register(ManagerModel)
class ManagerModel(admin.ModelAdmin):
    list_display=["id","name","city","designation","take_interview","hiring"]

@admin.register(Person)
class Person(admin.ModelAdmin):
    list_display=["id","name","city","email"]

@admin.register(Passport)
class Passport(admin.ModelAdmin):
    list_display=["id","user","pass_number","page","validity"]

@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display=["id","user","post_cap","post_details"]
    