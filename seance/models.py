from cProfile import label
from django.db import models
import datetime
from element.models import Element
from creneau.models import Creneau
# Create your models here.
class Seance(models.Model):
    date = models.DateField(default=datetime.date.today)
    type = models.CharField(max_length=255)
    creneau = models.ForeignKey(Creneau,unique=False,related_name="Creneau_Seance", on_delete=models.CASCADE)
    element = models.ForeignKey(Element,unique=False,related_name="Element_Seance", on_delete=models.CASCADE)


    
  
     