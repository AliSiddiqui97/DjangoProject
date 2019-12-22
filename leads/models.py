from django.db import models
from django.contrib.auth.models import User


class Lead(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name= models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc= models.TextField()
    price= models.IntegerField()
    offer=models.BooleanField(default=False)



