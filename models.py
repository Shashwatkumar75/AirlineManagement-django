from django.db import models
from datetime import date

# Create your models here.
class destination(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField(max_length=100)
    price=models.IntegerField()
    
    offer=models.BooleanField(default=False)
    validity=models.DateField(auto_now=False,auto_now_add=False,blank=True)
