from django.urls import path
from .views import  GestionPaginationFiliere, ProfesseurStats, ModuleStats
#from .views import GestionDepartementAll


urlpatterns = [
    path('all', GestionPaginationFiliere.as_view()),
    path('stats/professeurcount', ProfesseurStats.as_view()),
    path('stats/modulecount', ModuleStats.as_view()),
]

