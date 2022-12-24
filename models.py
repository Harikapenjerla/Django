from django.db import models

# Creating my models here.
class data(models.Model):
    User_Name = models.CharField(max_length=100)
    User_Contact = models.CharField(max_length=20)
    User_Address = models.CharField(max_length=200)

    #def __str__(self):
     #   return self.Name