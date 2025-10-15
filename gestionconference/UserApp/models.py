from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
import uuid
from django.core.exceptions import ValidationError 

def generate_user_id():
  return "USER"+ uuid.uuid4().hex[:5].upper()

def verify_email(email):
  domain = ["gmail.com","yahoo.com","outlook.com", "esprit.tn"]
  if email.split("@")[-1] not in domain:
    raise ValidationError("Invalid email domain")
  
name_validator = RegexValidator(regex=r'^[a-zA-Z\s-]+$', message='Only alphabetic characters are allowed.')


class User(AbstractUser):
  user_id = models.CharField(max_length=8, primary_key=True,unique=True,editable=False)
  first_name = models.CharField(max_length=30,validators=[name_validator])
  last_name = models.CharField(max_length=30,validators=[name_validator])
  email = models.EmailField(unique=True, validators=[verify_email])
  affiliation = models.CharField(max_length=100)
  ROLE=[
    ("participant","participant"),
    ("commitee","organizing commitee member"),


  ]
  role = models.CharField(max_length=20,choices=ROLE,default="participant")



  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)



  def save(self, *args, **kwargs):
    if not self.user_id:
      new_id = generate_user_id()
      while User.objects.filter(user_id=new_id).exists():
        new_id = generate_user_id()
      self.user_id = new_id    
    super().save(*args, **kwargs)
  
  def __str__(self):
        return f"{self.name} - {self.theme} ({self.start_date} to {self.end_date})"




 # submissions=models.ManyToManyField("ConferenceApp.Conference",through="ConferenceApp.Submission")
#  OrganizingCommiteeList = models.ManyToManyField("ConferenceApp.Conference",through="ConferenceApp.OrganizingCommitee")



class OrganizingCommitee(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE , related_name="commitees")

  conference = models.ForeignKey("ConferenceApp.Conference", on_delete= models.CASCADE , related_name="commitees")


  ROLES = [
    ("chair","chair"),
    ("co-chair" , "co-chair"),
    ("member" , "member")
  ]

  commitee_role = models.ForeignKey("ConferenceApp.Conference" , on_delete=models.CASCADE)

  date_joined = models.DateField(auto_now=True)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)