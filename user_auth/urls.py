from django.urls import path
from .views import *



urlpatterns = [
    path('',home,name='home'),
    path('login/',login_user,name='login_user'),
    path('logout/',logout_user,name='logout_user'),
    path('sign_up/',sign_up_user,name='sign_up_user'),

    # urls for Generate Password function
    path('generate_password/', generate_password, name='generate_password'),

]
