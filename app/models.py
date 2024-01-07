from django.db import models

class Student(models.Model):
    Name = models.CharField(max_length=20)
    RollNumber = models.CharField(max_length=10, default='0',blank=True, null=True)
    Department = models.CharField(max_length=5)
    Sem = models.CharField(max_length=5)
    Year = models.IntegerField()
    Sgpa = models.FloatField()
    Type = models.CharField(max_length=10)
