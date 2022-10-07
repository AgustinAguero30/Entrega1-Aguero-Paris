from django.urls import path
from AppLogin.views import *
from django.contrib.auth.views import LogoutView   

urlpatterns = [ 
    #Login
    path('', login_request, name= 'login'),
    #Logout
    path('logout/', LogoutView.as_view(template_name=('AppLogin/logout.html')), name='logout'),
    ]