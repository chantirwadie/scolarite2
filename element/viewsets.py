from rest_framework import viewsets
from .models import Element
from .  import serializers


class ElementViewset(viewsets.ModelViewSet):
    queryset =Element.objects.all()
    serializer_class = serializers.ElementSerializer
