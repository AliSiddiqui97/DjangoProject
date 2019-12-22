from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Destination(models.Model):
    
    name= models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc= models.TextField()
    price= models.IntegerField()
    offer=models.BooleanField(default=False)


class Testimonial(models.Model):
    testimony=models.CharField(max_length=1000)
    name=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    
class News(models.Model):
    
    day= models.IntegerField()
    month= models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    title= models.CharField(max_length=100)
    category= models.CharField(max_length=100)
    desc= models.CharField(max_length=700)
    
