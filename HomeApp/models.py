from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class register_form(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    firstname=models.CharField( max_length=50)
    lastname=models.CharField( max_length=50)
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    phone=models.CharField(max_length=50)
    pwd=models.CharField( max_length=50)
    cpwd=models.CharField( max_length=50)
    img=models.ImageField(upload_to='pics', height_field=None, width_field=None, max_length=None)
    gender=models.CharField(max_length=50,null=True)
    age = models.CharField(max_length=50,null=True)
    city = models.CharField( max_length=500,null=True)
    occupation = models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.user.username
    
    