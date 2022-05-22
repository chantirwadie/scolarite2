from django.urls import path
from .views import GestionDepartement, GestionPaginationDepartement
#from .views import GestionDepartementAll


urlpatterns = [
    path('', GestionDepartement.as_view()),
    path('all', GestionPaginationDepartement.as_view())
]

