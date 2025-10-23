

from django.urls import path
from .views import *


urlpatterns = [
  # path('get_all_conferences/', views.get_all_conferences, name='get_all_conferences'),
  path('get_all_conferences/', ConferenceList.as_view(), name='conference-list'),
  path('conference-details/<int:conference_id>/', ConferenceDetails.as_view(), name='conference-details'),
  path("form/",ConferenceCreate.as_view(),name="conference-add"),
  path("<int:pk>/update/",ConferenceUpdate.as_view(),name="conference-update"),
  path("<int:pk>/delete/",ConferenceDelete.as_view(),name="conference-delete"),



]