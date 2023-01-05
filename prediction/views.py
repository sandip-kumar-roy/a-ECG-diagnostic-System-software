from django.shortcuts import render
from HeartPredictApp.models import predict_form
# Create your views here.
def prediction_history(request):
    current_user=request.user
    prediction_history=predict_form.objects.filter(user_name=current_user)
    return render(request,'predict_history.html',{'context':prediction_history})