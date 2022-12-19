from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('profile', views.profile,name='profile'),
    path('about', views.about,name='about'),
    path('service', views.service,name='service'),
    path('team', views.team,name='team'),
    path('contact', views.contact,name='contact'),
    path('predform', views.predform,name='predform' ),
    path('register/', views.register,name='register' ),
    
]