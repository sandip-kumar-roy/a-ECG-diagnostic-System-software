from django.urls import path
from appointment import views
urlpatterns = [
    
    path('bookings', views.bookings,name='bookings'),
]