from rest_framework.routers import DefaultRouter

from gestionconference.ConferenceApp import admin

from .views import SessionViewSet
from django.urls import path, include


router = DefaultRouter()

router.register('sessions', SessionViewSet)
urlpatterns = [
  path('admin/',admin.site.urls),
  path('conference/',include('ConferenceApp.urls')),
  path('user/',include('UserApp.urls')),
  path('api/',include('SessionAPPApi.urls')),

]