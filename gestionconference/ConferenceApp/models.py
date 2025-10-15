from django.db import models
from django.core.validators import MinLengthValidator
from django.core.validators import FileExtensionValidator
# Create your models here.
class Conference(models.Model):
  conference_id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255)
  description = models.TextField(validators=[
    MinLengthValidator(limit_value=50 , message="la description doit contenir au min 50 chatactères ")
  ])
  location = models.CharField()
  THEMES = [
    ("CS&IA","Computer Science & IA"),
    ("SC" ,"Social Scinece" ),
    ("SE" , "Science and engineering"),
    ("ID" , "interdisciplinary")

  ]
  
  theme = models.CharField(choices=THEMES)

  start_time = models.DateTimeField()
  end_date = models.DateField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Submission(models.Model):
  submission_id =models.CharField(primary_key=True,unique=True)
  user = models.ForeignKey("UserApp.User", on_delete=models.CASCADE , related_name="submissions")
  conference = models.ForeignKey(Conference,on_delete=models.CASCADE,related_name="submissions")
  titre = models.CharField(max_length=255)
  abstract = models.TextField()
  keywords=models.TextField()
  paper = models.FileField(upload_to='sub_paper/', validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

  CHOICES = [
    ("submited", "submitted"),
    ("under review","under review"),
    ("accepted" , "accepted"),
    ("rejected" , "rejected")
  ]
  status=models.CharField(choices=CHOICES)

  payed = models.BooleanField(default=True)
  submission_date = models.DateTimeField(auto_now_add=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)