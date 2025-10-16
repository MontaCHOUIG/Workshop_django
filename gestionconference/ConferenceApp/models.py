from django.db import models
from django.core.validators import MinLengthValidator
from django.core.validators import FileExtensionValidator
from django.forms import ValidationError
import string
import random

# Custom validator for keywords
def validate_keywords_count(value):
    """Valide que le nombre de mots-clés ne dépasse pas 10"""
    if value:
        # Séparer les mots-clés par virgules et compter
        keywords_list = [keyword.strip() for keyword in value.split(',') if keyword.strip()]
        if len(keywords_list) > 10:
            raise ValidationError(
                f'Le nombre maximum de mots-clés est de 10. Vous en avez fourni {len(keywords_list)}.'
            )
        if len(keywords_list) == 0:
            raise ValidationError('Au moins un mot-clé est requis.')

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

  start_date = models.DateField()
  end_date = models.DateField()

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  def clean(self):
     if self.start_date > self.end_date:
       raise ValidationError("La date de fin doit être postérieure à la date de début.")



class Submission(models.Model):
  submission_id = models.CharField(primary_key=True, max_length=11, unique=True)
  user = models.ForeignKey("UserApp.User", on_delete=models.CASCADE , related_name="submissions")
  conference = models.ForeignKey(Conference,on_delete=models.CASCADE,related_name="submissions")
  titre = models.CharField(max_length=255)
  abstract = models.TextField()
  keywords=models.TextField(validators=[validate_keywords_count])
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
  
  def generate_submission_id(self):
    """Génère un ID de soumission unique au format SUBABCDEFGH"""
    while True:
      # Générer 8 caractères alphanumériques aléatoirement
      random_chars = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
      submission_id = f"SUB{random_chars}"
      
      # Vérifier que cet ID n'existe pas déjà
      if not Submission.objects.filter(submission_id=submission_id).exists():
        return submission_id
  
  def save(self, *args, **kwargs):
    # Générer l'ID seulement si c'est une nouvelle instance
    if not self.submission_id:
      self.submission_id = self.generate_submission_id()
    super().save(*args, **kwargs)
  
  def clean(self):
    if self.submission_date and self.conference:
      if self.submission_date.date() > self.conference.start_date:
          raise ValidationError("La date de soumission doit être antérieure à la date de début de la conférence.")

