from django.shortcuts import render
from .models import Filiere
from rest_framework.pagination import PageNumberPagination
from django.db.models import CharField
from django.db.models import  Q
from .serializers import Filieres
from rest_framework.response import Response
from rest_framework.views import APIView
from departement.models import Departement
from element.models import Element
from module.models import Module

# Create your views here.



class ProfesseurStats(APIView):

    # Getting the module 
    def get(self, request):
        result = []
        filieres = Filiere.objects.all()
        for filiere in filieres:
            modules = Module.objects.filter(filiere=filiere)
            for module in modules:
                count = 0
                elements = Element.objects.filter(module=module)
                for element in elements:
                    if(element.professeur is not None):
                        count += 1

                result.append({ 'name' : filiere.label , 'count' : count})        

        return Response(result) 

class ModuleStats(APIView):

    def get(self, request):
        result = []
        filieres = Filiere.objects.all()
        for filiere in filieres:
            modules = Module.objects.filter(filiere=filiere)
            if not modules:
                result.append({ 'name' : filiere.label , 'count' : 0})
            result.append({ "name" : filiere.label, "count" : modules.count() })
            

        return Response(result)                 

class GestionPaginationFiliere(APIView, PageNumberPagination):

    page_size = 1000
    page_size_query_param = 'page_size'
    page_number = 1
    page_number_query_param = "page"
    
    def get_queryset(self):

        filieres = Filiere.objects.all().order_by('id')
        query = self.request.GET.get('query', None)
        if query:
            fields = [f for f in Filiere._meta.fields if isinstance(f, CharField)]
            fieldsDepartement = [f for f in Filiere._meta.fields if isinstance(f, CharField)]
            queries = [Q(**{f.name + "__icontains" : query}) for f in fields]
            queriesDepartement = [Q(**{f.name + "__icontains" : query}) for f in fieldsDepartement]
            qs = Q()
            qsDepartement = Q()
            for query in queries:
                qs = qs | query 
            for query in queriesDepartement:
                qsDepartement = qsDepartement | query
            departement = Departement.objects.filter(qsDepartement)
            filieres2 = Filiere.objects.filter(departement__in=departement)
            filieres = Filiere.objects.filter(qs)
            filieres = filieres | filieres2
            
        queryset = Filieres(filieres, many=True) 
        return self.paginate_queryset(queryset.data, self.request)

    def get(self, request):
        filieres = self.get_queryset()

        print(filieres)
       
        # page_number = request.GET.get('page', 1)
        # page_obj = paginator.get_page(page_number)
        return self.get_paginated_response({"filieres": filieres})

    def post(self, request):

        ids = request.data.get('ids', None)

        if ids:
            Filiere.objects.filter(id__in=ids).delete()
            delete_count = len(ids)
            return Response({"message" : "%d filières supprimées avec succès" % delete_count})

        return Response({"message" : "Veuillez fournir un identifiant"}, 400)   