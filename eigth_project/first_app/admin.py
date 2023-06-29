from django.contrib import admin
from first_app.models import EmployeModels,ManagerModels,Friend,Me,Person,Passport,Post,Student,Teacher
# Register your models here.

# admin.site.register(EmployeModels)
# admin.site.register(ManagerModels)

# @admin.register(EmployeModels)
# class EmployeeModelAdmin(admin.ModelAdmin):
#     list_display = ['id','name','city','designation']
# @admin.register(ManagerModels)
# class ManagerModelAdmin(admin.ModelAdmin):
#     list_display = ['id','name','city','designation','take_interview','hiring']


# @admin.register(Friend)
# class FriendModelAdmin(admin.ModelAdmin):
#     list_display = ['id','school','section','attendance','hw']
    

# @admin.register(Me)
# class FriendModelAdmin(admin.ModelAdmin):
#     list_display = ['id','school','section','attendance','hw']
# @admin.register(Person)
# class PersonModelAdmin(admin.ModelAdmin):
#     list_display = ['id','name','cities','email']
    
# @admin.register(Post)
# class PostModelAdmin(admin.ModelAdmin):
#     list_display = ['id','user','post_cap','post_details']

# @admin.register(Passport)
# class FriendModelAdmin(admin.ModelAdmin):
#     list_display = ['id','user','pass_number','page','validity']


@admin.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','class_name']
    
@admin.register(Teacher)
class TeacherModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','subject','student_list','mobiles']