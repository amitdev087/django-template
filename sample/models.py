from django.db import models

# Create your models here.

class Students(models.Model):
    firstName=models.CharField(max_length=100)
    lastName=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    rollNumber=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)


    def __str__(self):
        return self.firstName+" " + self.lastName
