from django.urls import path
from .views import *

urlpatterns = [
    path('', homePage, name="Home_Page"),
    path('listStatic/', listEventsStatic, name="events_list_static"),
    path('list/', listEvents, name="events_list"),
    path('add/', addEvent, name="events_add"),
    path('details/<int:id>', detailsEvent, name="events_details"),
    path('part/<int:id>', participateEvent, name="events_Participate"),
     path('cancelPart/<int:id>', CancelParticipate, name="cancel_Participate"),
    path('update/<int:pk>', EventupdateView.as_view(), name="events_update"),
    path('listEvents/', EventsList.as_view(), name="events_listC"),
    path('delete/<int:pk>', EventDeleteView.as_view(), name="events_delete"),
    path('eventsDetails/<int:pk>', EventsDetails.as_view(), name="events_DetailsC"),
]
