from departement.viewsets import DepartementViewset
from filliere.viewsets import FiliereViewset
from module.viewsets import ModuleViewset
from element.viewsets import ElementViewset
from creneau.viewsets import CreneauViewset
from cahierText.viewsets import CahierTextViewset
from seance.viewsets import SeanceViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('v2/departement',DepartementViewset)
router.register('v2/filiere',FiliereViewset)
router.register('v2/module',ModuleViewset)
router.register('v2/creneau',CreneauViewset)
router.register('v2/seance',SeanceViewset)
router.register('v2/cahierText',CahierTextViewset)
