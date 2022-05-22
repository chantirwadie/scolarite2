from django.db import models

# Create your models here.


class anneeUniversitaire(models.Model):

    label = models.CharField(max_length=255,unique=True, blank=False, error_messages={
        "unique" : "label must be unique"
    })
    dateDebut = models.DateField()
    dateFin = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.label