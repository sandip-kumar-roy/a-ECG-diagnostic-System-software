from django.contrib import admin
from appointment.models import create_appointment
# Register your models here.
class create_appointmentAdmin(admin.ModelAdmin):
    list_display = ["usr_id","doctor_name","doctor_id","invoice_id","status","processed_on"]
admin.site.register(create_appointment,create_appointmentAdmin)

