from django.shortcuts import render
from search.models import locate_city
from appointment.models import create_appointment
from django.conf import settings
from decimal import Decimal

# Create your views here.
from django.forms.models import model_to_dict
def bookings(request):
    current_user=request.user
    payment_history=create_appointment.objects.filter(usr_id=current_user.id)
    return render(request,'history.html',{"context":payment_history})


