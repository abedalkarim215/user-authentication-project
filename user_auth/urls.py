from django.urls import path
from .views import *



urlpatterns = [
    path('',home,name='home'),
    path('login/',login_user,name='login_user'),
    path('logout/',logout_user,name='logout_user'),
    path('sign_up/',sign_up_user,name='sign_up_user'),
    path('delete_account/',delete_account,name='delete_account'),
    path('change_password/',change_password,name='change_password'),
    path('edit/',edit_information,name='edit_information'),

    # urls for Generate Password function
    path('generate_password/', generate_password, name='generate_password'),

]
