from cProfile import label
from django.db import models

# Create your models here.
class Departement(models.Model):
    nom = models.CharField(max_length=255)
    label = models.CharField(max_length=255,unique=True, blank=False, error_messages={
        "unique" : "label must be unique"
    })
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
     