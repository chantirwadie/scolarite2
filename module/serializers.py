from rest_framework import serializers
from .models import Module
from filliere.serializers import FiliereSerializer
from element.models import Element

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'

    def create(self, validated_data):
        module = Module.objects.create(**validated_data)

        element_data = {'nom' : validated_data.get('nom') , 'label' : validated_data.get('label'), 
        'pourcentage_module' : 100.0, 'pourcentage_element' : 100.0, 'pourcentage_controle' : 60.0 , 'module' : module}

        ## Creating Element object
        Element.objects.create(**element_data)


        return module


class Modules(serializers.ModelSerializer):

    filiere = FiliereSerializer()   

    class Meta:
        model = Module
        fields = '__all__'
        