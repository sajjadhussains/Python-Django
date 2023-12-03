from django.db import models

# Create your models here.

# class Movie(models.Model):
#     movie_title = models.CharField(max_length=20)
#     release_year = models.IntegerField()

class Student(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField(primary_key=True)
    address = models.TextField()

    def __str__(self):
        return f"Roll:{self.roll}-{self.name}"