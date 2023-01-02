from django.urls import path

from django.contrib.auth.views import LoginView
from . import views
urlpatterns = [
    path('', views.home),
    
    path('msg', views.msg,name='msg'),
    path('profile', views.profile,name='profile'),
    path('about', views.about,name='about'),
    path('service', views.service,name='service'),
    path('team', views.team,name='team'),
    path('newpwd', views.newpwd,name='newpwd'),
    path('reset', views.reset,name='reset'),
    path('register/', views.register,name='register' ),
    path('check_user/', views.check_user,name='check_user' ),
    path('user_login', views.user_login,name='user_login' ),
    path('user_logout', views.user_logout,name='user_logout' ),
    path('reset_pwd_page', views.reset_pwd_page,name='reset_pwd_page'),
    
]