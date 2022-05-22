from cProfile import label
from django.db import models
from module.models import Module

# Create your models here.
class Element(models.Model):
    nom = models.CharField(max_length=255)
    label = models.CharField(max_length=255,unique=True, blank=False, error_messages={
        "unique" : "label must be unique"
    })
    categorie = models.CharField(max_length=255)
    semestre = models.CharField(max_length=255)
    pourcentage_element = models.FloatField(max_length=50,blank=True)
    heures = models.FloatField(max_length=50,default=0.0)
    pourcentage_controle = models.FloatField(max_length=50)
    pourcentage_module = models.FloatField(max_length=50)
    module = models.ForeignKey(Module,unique=False,related_name="Module_element", on_delete=models.CASCADE)
    professeur = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
