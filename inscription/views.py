from django.shortcuts import render
import urllib3
# Create your views here.
from .models import Inscription
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import InscriptionSerializer
import traceback
import json
from django.http import JsonResponse
from django.conf import settings

http = urllib3.PoolManager()

class InscriptionAdd(APIView):
    """ This class will handle the add of a new inscription """
    def post(self, request):
        serializer = InscriptionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class GestionInscription(APIView):
    """ This class will handle the CRUD OPERATIONS EXCEPT ADD"""
    def get(self, request, id):
        inscription = Inscription.objects.filter(pk=id).first()
        if inscription:
            serializer = InscriptionSerializer(inscription)
            return Response(serializer.data)
        return Response({"message" : "Ancunne inscription existe avec l'identifiant donné"}, 400)

    def put(self,request, id):
        inscriptionObject = Inscription.objects.filter(pk=id).first()
        serializer = InscriptionSerializer().update(inscriptionObject, request.data)
        
        return Response(InscriptionSerializer(serializer).data, 200)
       
    def delete(self, request, id):
        try:
            inscriptionObject = Inscription.objects.filter(pk=id).first()
            Inscription.objects.filter(pk=inscriptionObject.id).delete()
            return Response({"message" : "Deleted successfully"})
        except Exception as e:
            m = traceback.format_exc()    
            return Response({"message" : m}, 404)            



class GetAllInscriptions(APIView):

    def get(self, request):
        
        queryset = InscriptionSerializer(Inscription.objects.all(), many=True)
        print(len(queryset.data))
        for i in range(len(queryset.data)):
            idEtudiant = queryset.data[i]["etudiant"]
            url=settings.API_GATE_WAY+"/api/v1/etudiant"
            final_url= '/'.join([url,str(idEtudiant)])
            r = http.request('GET',final_url)
            data=json.loads(r.data)
            queryset.data[i]["etudiant"]=data
        return Response( queryset.data)