from django.contrib import admin
from django.urls import path,include
from.import views
from uapp import views

urlpatterns = [
    path('',views.login_user,name='login'),
    path('signin',views.signin,name='signin'),
    path('welcome',views.main,name='main'),
    
]
