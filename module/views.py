from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import urllib3
import json
from .models import Module
from filliere.models import Filiere
from rest_framework.pagination import PageNumberPagination
from django.db.models import CharField
from django.db.models import  Q
from .serializers import Modules
from departement.models import Departement

# Create your views here.
http = urllib3.PoolManager()

class TestView(APIView):
    def get(self, request):
        r = http.request('GET', 'http://localhost:8000/api/v1/professeur/2')
        data = json.loads(r.data)
        return Response({"message": "Hello World"})

class GestionPaginationModule(APIView, PageNumberPagination):

    page_size = 1000
    page_size_query_param = 'page_size'
    page_number = 1
    page_number_query_param = "page"
    
    def get_queryset(self):

        modules = Module.objects.all().order_by('id')
        query = self.request.GET.get('query', None)
        if query:
            fields = [f for f in Module._meta.fields if isinstance(f, CharField)]
            fieldsDepartement = [f for f in Module._meta.fields if isinstance(f, CharField)]
            queries = [Q(**{f.name + "__icontains" : query}) for f in fields]
            queriesDepartement = [Q(**{f.name + "__icontains" : query}) for f in fieldsDepartement]
            qs = Q()
            qsDepartement = Q()
            for query in queries:
                qs = qs | query 
            for query in queriesDepartement:
                qsDepartement = qsDepartement | query
            filiere = Filiere.objects.filter(qsDepartement)
            modules2 = Module.objects.filter(filiere__in=filiere)
            modules = Module.objects.filter(qs)
            modules = modules | modules2
            
        queryset = Modules(modules, many=True) 
        return self.paginate_queryset(queryset.data, self.request)

    def get(self, request):
        modules = self.get_queryset()       
        # page_number = request.GET.get('page', 1)
        # page_obj = paginator.get_page(page_number)
        return self.get_paginated_response({"modules": modules})

    def post(self, request):

        ids = request.data.get('ids', None)

        if ids:
            Module.objects.filter(id__in=ids).delete()
            delete_count = len(ids)
            return Response({"message" : "%d modules supprimés avec succès" % delete_count})

        return Response({"message" : "Veuillez fournir un identifiant"}, 400)           