from cProfile import label
from django.db import models
from departement.models import Departement

# Create your models here.
class Filiere(models.Model):
    nom = models.CharField(max_length=255)
    label = models.CharField(max_length=255,unique=True, blank=False, error_messages={
        "unique" : "label must be unique"
    })
    
     # Relation to departement
    departement = models.ForeignKey(Departement,unique=False,related_name="Departement_filliere", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
