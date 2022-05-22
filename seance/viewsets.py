from rest_framework import viewsets
from .models import Seance
from .  import serializers

class SeanceViewset(viewsets.ModelViewSet):
    queryset =Seance.objects.all()
    serializer_class = serializers.SeanceSerializer