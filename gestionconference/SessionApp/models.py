from django.db import models
from django.forms import ValidationError
from ConferenceApp.models import Conference
# Create your models here.
from django.core.validators import RegexValidator

room_validator = RegexValidator(regex=r'^[A-Za-z0-9\s-]+$', message='Only alphanumeric characters, spaces, and hyphens are allowed in the room name.')


class Session(models.Model):
  session_id = models.CharField(primary_key=True)
  title = models.CharField(max_length=255)
  topix = models.CharField(max_length=255)
  session_day = models.DateField()
  start_time = models.TimeField()
  end_time = models.TimeField()

  room = models.CharField(max_length=255)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  conference = models.ForeignKey("ConferenceApp.Conference",on_delete=models.CASCADE,related_name="sessions")
# Create your models here.


  def clean(self):
    if self.session_day < self.conference.start_date or self.session_day > self.conference.end_date:
        raise ValidationError("La date de la session doit être comprise entre les dates de début et de fin de la conférence.")
    if self.start_time >= self.end_time:
        raise ValidationError("L'heure de début doit être antérieure à l'heure de fin.")
    