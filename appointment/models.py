from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class create_appointment(models.Model):
    usr_id=models.ForeignKey(User, on_delete=models.CASCADE)
    doctor_name=models.CharField( max_length=250)
    doctor_id=models.CharField( max_length=250)
    invoice_id=models.CharField(max_length=50)
    status=models.BooleanField(default=False)
    processed_on=models.DateTimeField( auto_now_add=True)

  

