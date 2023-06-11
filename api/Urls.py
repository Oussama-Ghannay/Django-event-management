from django.urls import path
from .Views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
      path('get',getEvents , name="getevent"),
      

]
