from rest_framework import viewsets
from .models import Departement
from .  import serializers


class DepartementViewset(viewsets.ModelViewSet):
    queryset =Departement.objects.all()
    serializer_class = serializers.DepartementSerializer
