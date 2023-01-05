from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
urlpatterns = [
    path('search', views.search,name='search'),
    path('book/<int:id>', views.book, name='book'),
    path('payment-done', views.payment_done, name='payment_done'),
    path('payment-cancelled', views.payment_cancelled, name='payment_cancelled'),
]