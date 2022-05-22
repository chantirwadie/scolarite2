from rest_framework import viewsets
from .models import CahierText
from .  import serializers


class CahierTextViewset(viewsets.ModelViewSet):
    queryset =CahierText.objects.all()
    serializer_class = serializers.CahierTextSerializer
