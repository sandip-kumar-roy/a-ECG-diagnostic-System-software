from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class predict_form(models.Model):
    user_name=models.CharField(max_length=50,null=True)
    age=models.IntegerField()
    Chest_pain_type=models.CharField( max_length=50)
    resting_blood_pressure=models.IntegerField()
    serum_cholestoral=models.IntegerField()
    fasting_blood_sugar=models.CharField(max_length=50)
    resting_electrocardiographic=models.CharField( max_length=50)
    max_heart_rate=models.IntegerField()
    exercise_induced_angina=models.ImageField(upload_to='pics', height_field=None, width_field=None, max_length=None)
    oldpeak=models.FloatField(null=True)
    peak_ST_segment_slope = models.CharField(max_length=50,null=True)
    major_vessels = models.IntegerField(null=True)
    thal  = models.CharField(max_length=50,null=True)
    Gender=models.CharField( max_length=50)
    added_on=models.DateTimeField( auto_now_add=True,null=True)
    result=models.CharField(null=True,max_length=50)
    
    def __str__(self):
        return self.user_name
    
    
    
    