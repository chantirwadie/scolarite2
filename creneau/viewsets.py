from rest_framework import viewsets
from .models import Creneau
from .  import serializers


class CreneauViewset(viewsets.ModelViewSet):
    queryset =Creneau.objects.all()
    serializer_class = serializers.CreneauSerializer
