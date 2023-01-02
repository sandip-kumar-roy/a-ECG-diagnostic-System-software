from django.db import models

# Create your models here.
class locate_city(models.Model):
    img=models.ImageField(upload_to='pics', height_field=None,null=True, width_field=None, max_length=None)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50,null=True)
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    address=models.TextField(null=True)
    occupation=models.TextField(null=True)

