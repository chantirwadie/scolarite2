from cProfile import label
from django.db import models

# Create your models here.
class Creneau(models.Model):
    heure_debut = models.CharField(max_length=255)
    heure_fin = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
  
     