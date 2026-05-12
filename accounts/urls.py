from django.urls import path
from .views import (
 
    register,
    user_login,
    user_list
 
    
)
 
urlpatterns = [
 
    path('register/', register),
 
    path('login/', user_login),
 
    path('users/', user_list)
 
    
    
    
    
]
