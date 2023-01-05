from django.urls import path
from . import views
urlpatterns = [
    path('prediction_history', views.prediction_history,name='prediction_history'),
    
]