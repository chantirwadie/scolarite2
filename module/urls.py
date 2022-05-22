from django.urls import path
from .views import TestView, GestionPaginationModule


urlpatterns = [
    path('service', TestView.as_view()),
    path('all', GestionPaginationModule.as_view()),
]
