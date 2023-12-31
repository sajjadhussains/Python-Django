from django.db import models

# Create your models here.

class StudentModel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=30)
    address = models.TextField()
    
    def __str__(self):
        return f"{self.roll}-{self.name}"

class CommonInfoClass(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length = 50)
    class Meta:
        abstract = True

class StudentInfoModel(CommonInfoClass):
    roll = models.IntegerField()
    payment = models.IntegerField()
    section = models.CharField(max_length=20)

class TeacherInfoModel(CommonInfoClass):
    salary = models.IntegerField()


class EmployeeModel(models.Model):
    name=models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    designation = models.CharField(max_length=30)

class ManagerModel(EmployeeModel):
    take_interview = models.BooleanField()
    hiring = models.BooleanField()
    
class Person(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    def __str__(self):
        return self.name

class Passport(models.Model):
    user = models.OneToOneField(to=Person,on_delete=models.CASCADE)
    pass_number = models.IntegerField()
    page = models.IntegerField()
    validity = models.IntegerField()

#one to many relationship
class Post(models.Model):
    user = models.ForeignKey(Person,on_delete=models.SET_NULL,null=True)
    post_cap=models.CharField(max_length=40)
    post_details=models.CharField(max_length=100)
    
# many to many relationship

class Student(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField()
    class_name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Teacher(models.Model):
    student = models.ManyToManyField(Student,related_name="teachers")
    name = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
    mobile = models.CharField(max_length=11)
    def student_list(self):
        return ",".join([str(i) for i in self.student.all()])