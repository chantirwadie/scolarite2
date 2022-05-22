from rest_framework import viewsets
from .models import Filiere
from .  import serializers


class FiliereViewset(viewsets.ModelViewSet):
    queryset =Filiere.objects.all()
    serializer_class = serializers.FiliereSerializer
