from django.urls import path
from . import views
urlpatterns = [
    path('locate', views.locate,name='locate'),
    path('reg', views.reg,name='reg'),
    path('prdictformpage', views.prdictformpage,name='prdictformpage'),
    path('result_page', views.result_page,name='result_page'),
    path('edit_form', views.edit_form,name='edit_form'),
    path('save_form', views.save_form,name='save_form'),
    
]