from .models import Departement
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import DepartementSerializer
import traceback
from rest_framework.pagination import PageNumberPagination
from django.db.models import CharField
from django.db.models import  Q

# Create your views here.


class GestionDepartement(APIView):
    """ This class will handle the CRUD OPERATIONS"""

    def post(self, request):
        serializer = DepartementSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def get(self, request):
        departement = Departement.objects.all()
   
        departement_serialized = DepartementSerializer(departement).data
        return Response({
            "departement" : departement_serialized,
        })
    

    def put(self,request):
        try:
            Departement.objects.filter(pk=request.data["id"]).update(**request.data)
            return Response({"message" : "successfully updated"}, 200)
        except Exception as e:
            m = traceback.format_exc()
            return Response({"message" : m}, 404) 
    def delete(self, request):
        try:
            Departement.objects.filter(pk=request.data["id"]).delete()
            return Response({"message" : "Deleted successfully"})
        except Exception as e:
            m = traceback.format_exc()    
            return Response({"message" : m}, 404)            


class GestionPaginationDepartement(APIView, PageNumberPagination):

    page_size = 1000
    page_size_query_param = 'page_size'
    page_number = 1
    page_number_query_param = "page"
    
    def get_queryset(self):

        departements = Departement.objects.all().order_by('id')
        query = self.request.GET.get('query', None)
        if query:
            fields = [f for f in Departement._meta.fields if isinstance(f, CharField)]
            queries = [Q(**{f.name + "__icontains" : query}) for f in fields]
            qs = Q()
            for query in queries:
                qs = qs | query 
            departements = Departement.objects.filter(qs)
            
        queryset = DepartementSerializer(departements, many=True) 
        return self.paginate_queryset(queryset.data, self.request)

    def get(self, request):
        departements = self.get_queryset()
        return self.get_paginated_response({"departements": departements})

    def post(self, request):
        ids = request.data.get('ids', None)
        if ids:
            Departement.objects.filter(id__in=ids).delete()
            delete_count = len(ids)
            return Response({"message" : "%d departements supprimés avec succès" % delete_count})

        return Response({"message" : "Veuillez fournir un identifiant"}, 400)     

    