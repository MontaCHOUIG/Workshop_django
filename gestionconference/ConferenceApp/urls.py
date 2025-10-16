

from django.urls import path
from . import views

urlpatterns = [
   path('get_all_conferences/', views.get_all_conferences, name='get_all_conferences'),
]