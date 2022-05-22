from .models import Element
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ElementSerializer,ElementAddSerializer
import traceback
from django.http import JsonResponse
import urllib3
import json
from rest_framework.pagination import PageNumberPagination
from django.db.models import CharField
from django.db.models import  Q
from module.models import Module
from filliere.models import Filiere
from django.conf import settings

# Create your views here.
http = urllib3.PoolManager()


class ElementAdd(APIView):
    """ This class will handle the add of a new etudiant """
    def post(self, request):
   
        serializer = ElementAddSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data})


class GestionElement(APIView):
    """ This class will handle the CRUD OPERATIONS EXCEPT ADD"""
    def get(self, request, id):
        element = Element.objects.filter(pk=id).first()
        if element:
            serializer = ElementSerializer(element)
            idProfessseur = serializer.data['professeur']
            if idProfessseur is not None:
                url = settings.API_GATE_WAY+'/api/v1/professeur' 
                final_url = '/'.join([url, str(idProfessseur)])
                r = http.request('GET', final_url)
                data = json.loads(r.data)
                serializer.data['professeur']=data
            return Response({"element": serializer.data})
        return Response({"message" : "Ancun element existe avec l'identifiant donné"}, 400)

    def put(self,request, id):
        elementObject = Element.objects.filter(pk=id).first()
        serializer = ElementAddSerializer().update(elementObject, request.data)
        return Response(ElementAddSerializer(serializer).data, 200)
       
    def delete(self, request, id):
        try:
            etudiantObject = Element.objects.filter(pk=id).delete()
            return Response({"message" : "Deleted successfully"})
        except Exception as e:
            m = traceback.format_exc()    
            return Response({"message" : m}, 404)            


  


class GetAllElement(APIView, PageNumberPagination):

    page_size = 1000
    page_size_query_param = 'page_size'
    page_number = 1
    page_number_query_param = "page"

    def get_queryset(self):
        # product_sync_ts = self.request.GET.get('product_sync_ts', None)
        # if product_sync_ts:
        #     products = Etudiant.objects.filter(update_ts__gt=product_sync_ts)
        elements = Element.objects.all().order_by('id')
        query = self.request.GET.get('query', None)
        if query:
            fields = [f for f in Element._meta.fields if isinstance(f, CharField)]
            fieldsUser = [f for f in Module._meta.fields if isinstance(f, CharField)]
            queries = [Q(**{f.name + "__icontains" : query}) for f in fields]
            queriesUser = [Q(**{f.name + "__icontains" : query}) for f in fieldsUser]
            qs = Q()
            qsUser = Q()
            for query in queries:
                qs = qs | query
            for query in queriesUser:
                qsUser = qsUser | query    
            elements = Element.objects.filter(qs)
            modules = Module.objects.filter(qsUser).all().order_by('id')
            elements2 = Element.objects.filter(module__in=modules)
            elements  = elements2 | elements

        queryset = ElementSerializer(elements, many=True) 
        for i in range(len(queryset.data)):
            idProfesseur = queryset.data[i]['professeur']
            if idProfesseur is not None:
                url = settings.API_GATE_WAY+'/api/v1/professeur'  # no trailing /
                final_url = '/'.join([url, str(idProfesseur)])
                r = http.request('GET', final_url)
                data = json.loads(r.data)
                queryset.data[i]['professeur']=data['professeur'] 
        return self.paginate_queryset(queryset.data, self.request)    

    def get(self, request):
        elements = self.get_queryset()
        return self.get_paginated_response(elements)

    def post(self, request):

        ids = request.data.get('ids', None)

        if ids:
            Element.objects.filter(id__in=ids).delete()
            delete_count = len(ids)
            return Response({"message" : "%d elements supprimés avec succès" % delete_count})

        return Response({"message" : "Veuillez fournir un identifiant"}, 400)    