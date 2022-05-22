from cProfile import label
from django.db import models
from filliere.models import Filiere

# Create your models here.
class Module(models.Model):
    nom = models.CharField(max_length=255)
    label = models.CharField(max_length=255,unique=True, blank=False, error_messages={
        "unique" : "label must be unique"
    })
    
     # Relation to departement
    filiere= models.ForeignKey(Filiere,unique=False,related_name="filliere_module", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
