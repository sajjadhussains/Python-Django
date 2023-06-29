from django.db import models

# Create your models here.

#multitable_inheritance

class EmployeModels(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=30)
    designation = models.CharField(max_length=20)
    
class ManagerModels(EmployeModels):
    take_interview = models.BooleanField()
    hiring = models.BooleanField()

#----Proxy  
class Friend(models.Model):
    school = models.CharField(max_length=20)
    section = models.CharField(max_length=15)
    attendance = models.BooleanField()
    hw = models.CharField(max_length=50)
class Me(Friend):
    class Meta:
        proxy = True
        ordering =['id']

# one to one relation in Django

class Person(models.Model):
    name = models.CharField(max_length=20)
    cities = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    def __str__(self):
        return self.name
    
class Passport(models.Model):
    user = models.OneToOneField(to=Person,on_delete = models.CASCADE)
    pass_number = models.IntegerField()
    page = models.IntegerField()
    validity = models.IntegerField()  

# one to many or many to one relationship.
# when a facebook user can multiple task or multiple post,that time this relation used

class Post(models.Model):
    user = models.ForeignKey(Person,on_delete=models.SET_NULL,null=True)
    post_cap = models.CharField(max_length=40)
    post_details = models.CharField(max_length=100)
    
##Many to Many relationship

class Student(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField()
    class_name = models.CharField(max_length=10)
    def __str__(self) -> str:
        return self.name

class Teacher(models.Model):
    student = models.ManyToManyField(Student,related_name='teachers')
    name = models.CharField(max_length=30)
    subject = models.CharField(max_length=20)
    mobiles = models.CharField(max_length=11)
    def student_list(self):
        return ",".join([str(i) for i in self.student.all()])
    def __str__(self) -> str:
        return self.name
    


    
