from rest_framework import serializers
from .models import Seance
class SeanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seance
        fields = '__all__'
        