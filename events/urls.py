from django.urls import path
from .views import *
urlpatterns = [
    path('',homePage,name="Home_Page"),
    path('listStatic/',listEventsStatic,name="events_list_static"),
    path('listevent/',listEvents,name="events_list"),

]


