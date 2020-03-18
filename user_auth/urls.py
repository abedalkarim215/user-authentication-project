from django.urls import path
from .views import *



urlpatterns = [
    path('',home,name='home'),
    path('login/',login_user,name='login_user'),
    path('logout/',logout_user,name='logout_user'),
]
