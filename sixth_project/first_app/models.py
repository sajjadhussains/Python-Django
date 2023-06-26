from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20)
    rools = models.IntegerField(primary_key=True)
    address = models.TextField()
    fathers_name = models.TextField(default="Rahim")
    
    def __str__(self) -> str:
        return f"Name:{self.name} Rool:{self.rools} Address:{self.address}"