from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class contact_form(models.Model):
    firstnm=models.CharField( max_length=50)
    lastnm=models.CharField( max_length=50)
    mail=models.CharField( max_length=50)
    contact=models.CharField( max_length=50)
    mesg=models.TextField()

    def __str__(self):
        return firstnm


