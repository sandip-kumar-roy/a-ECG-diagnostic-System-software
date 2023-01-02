from django.contrib import admin
from HeartPredictApp.models import predict_form
class predict_formAdmin(admin.ModelAdmin):
    
    list_display = ["user_name","age","Chest_pain_type","resting_blood_pressure","serum_cholestoral","fasting_blood_sugar","resting_electrocardiographic","max_heart_rate","exercise_induced_angina","oldpeak","peak_ST_segment_slope","major_vessels","thal","Gender"]
    search_fields = ["user_name"]
  
    
admin.site.register(predict_form,predict_formAdmin) 