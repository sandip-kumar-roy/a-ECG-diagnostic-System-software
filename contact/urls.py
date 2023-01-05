from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
urlpatterns = [
    path('contact_us', views.contact_us,name='contact_us'),
    
    
]