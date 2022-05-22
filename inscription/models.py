
from django.db import models
from filliere.models import Filiere
from anneeUniversitaire.models import anneeUniversitaire
# Create your models here.

class Inscription(models.Model):

    #User 

    etudiant = models.IntegerField()
    
    # Relation to filliere
    filiere= models.ForeignKey(Filiere,unique=False,related_name="filiere_inscription", on_delete=models.CASCADE)

    # ANNEE
    anneeUniversitaire = models.ForeignKey(anneeUniversitaire, related_name="anneeUniversitaire_inscription", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

