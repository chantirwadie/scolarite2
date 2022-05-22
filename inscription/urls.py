from django.urls import path
from .views import InscriptionAdd, GetAllInscriptions, GestionInscription


urlpatterns = [
    path('', InscriptionAdd.as_view()),
    path('all', GetAllInscriptions.as_view()),
    #path('<int:id>', GestionInscription.as_view())
]

