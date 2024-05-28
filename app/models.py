from django.db import models

# Create your models here.
class Student(models.Model):
    sname = models.CharField(primary_key=True, max_length=100)

    sage = models.IntegerField()
    semail = models.EmailField()
    spassword = models.CharField(max_length=100)
    # address = models.TextField()
    # hobby = models.CharField(max_length=100)
    # school_type = models.CharField(max_length=50)
    # school_logo = models.FileField(upload_to='logos/')

    def __str__(self):
        return self.sname

class Guradian(models.Model):
    gname = models.CharField(max_length=100)
    gemail = models.EmailField()
    sname = models.ForeignKey(Student, on_delete=models.CASCADE)
    email=models.EmailField()