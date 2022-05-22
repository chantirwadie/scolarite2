from django.urls import path
from .views import GestionAnneeUniversitaire, GestionPaginationAnneeUniversitaire
#from .views import GestionAnneeUniversitaireAll


urlpatterns = [
    path('', GestionAnneeUniversitaire.as_view()),
    path('all', GestionPaginationAnneeUniversitaire.as_view())
]

