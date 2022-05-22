from rest_framework import serializers

from .models import anneeUniversitaire

class AnneeUniversitaireSerializer(serializers.ModelSerializer):

    class Meta:
        model = anneeUniversitaire
        fields = '__all__'

