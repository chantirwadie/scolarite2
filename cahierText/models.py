from cProfile import label
from django.db import models
import datetime
from seance.models import Seance


# Create your models here.
class CahierText(models.Model):
    titre = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date = models.DateField(default=datetime.date.today)
     # Relation to seance
    seance= models.OneToOneField(Seance,unique=True,related_name="seance", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    