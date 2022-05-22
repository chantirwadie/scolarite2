from rest_framework import viewsets
from .models import Module
from .  import serializers


class ModuleViewset(viewsets.ModelViewSet):
    queryset =Module.objects.all()
    serializer_class = serializers.ModuleSerializer
