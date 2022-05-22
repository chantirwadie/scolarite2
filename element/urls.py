from django.urls import path
from .views import ElementAdd, GetAllElement, GestionElement


urlpatterns = [
    path('', ElementAdd.as_view()),
    path('all', GetAllElement.as_view()),
    path('<int:id>', GestionElement.as_view()),
]

