from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
urlpatterns = [
    path('search', views.search,name='search'),

]