from rest_framework import serializers

from departement.serializers import DepartementSerializer
from .models import Filiere
from departement.models import Departement

class FiliereSerializer(serializers.ModelSerializer):

    departement = serializers.PrimaryKeyRelatedField(queryset=Departement.objects.all(), many=False)
    class Meta:
        model = Filiere
        fields = '__all__'



class Filieres(serializers.ModelSerializer):

    departement = DepartementSerializer()

    class Meta:
        model = Filiere
        fields = '__all__'