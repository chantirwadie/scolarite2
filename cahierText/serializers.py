
from rest_framework import serializers
from .models import CahierText

class CahierTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = CahierText
        fields = '__all__'
        