from rest_framework import serializers
from .models import Creneau

class CreneauSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creneau
        fields = '__all__'
        