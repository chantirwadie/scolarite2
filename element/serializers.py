from module.models import Module
from xml.dom.minidom import Element
from module.serializers import ModuleSerializer
from rest_framework import serializers
from .models import Element

class ElementSerializer(serializers.ModelSerializer):
    module = ModuleSerializer()
    class Meta:
        model = Element
        fields = '__all__'
    def update(self, instance, validated_data):
        
        instance.nom = validated_data.get('nom', instance.nom)
        instance.label = validated_data.get('label', instance.label)
        instance.categorie = validated_data.get('categorie', instance.categorie)
        instance.semestre = validated_data.get('semestre', instance.semestre)
        instance.pourcentage_element = validated_data.get('pourcentage_element', instance.pourcentage_element)
        instance.pourcentage_controle = validated_data.get('pourcentage_controle', instance.pourcentage_controle)
        instance.pourcentage_module = validated_data.get('pourcentage_module', instance.pourcentage_module)
        instance.module = validated_data.get('module', instance.module)
        instance.professeur = validated_data.get('professeur', instance.professeur)

        instance.save()
        return instance
class ElementAddSerializer(serializers.ModelSerializer):
    module = serializers.PrimaryKeyRelatedField(queryset=Module.objects.all(), many=False)
    class Meta:
            model = Element
            fields = '__all__'

    def update(self, instance, validated_data):
        
        instance.nom = validated_data.get('nom', instance.nom)
        instance.label = validated_data.get('label', instance.label)
        instance.categorie = validated_data.get('categorie', instance.categorie)
        instance.semestre = validated_data.get('semestre', instance.semestre)
        instance.pourcentage_element = validated_data.get('pourcentage_element', instance.pourcentage_element)
        instance.pourcentage_controle = validated_data.get('pourcentage_controle', instance.pourcentage_controle)
        instance.pourcentage_module = validated_data.get('pourcentage_module', instance.pourcentage_module)

        module_id = validated_data.get('module')
        if module_id is not None:
            instance.module = Module.objects.get(id=module_id)    
        instance.professeur = validated_data.get('professeur', instance.professeur)    
        instance.save()    
        return instance
    