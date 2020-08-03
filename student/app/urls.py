from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup',views.handleSignup,name='handleSignup'),
    path('login',views.handleLogin,name='handleLogin'),
    path('forgotpassword',views.handleForgotpassword,name='handleForgotpassword'),
    path('handlelogout',views.handlelogout,name='handlelogout'),
]