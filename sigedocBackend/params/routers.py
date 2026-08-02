from rest_framework.routers import DefaultRouter
from .views import *
from params import views

router = DefaultRouter()
#____________________URLs___________________________________________________
router.register('formulaires',      FormulaireViewset,       basename='formulaires')
router.register('diplome_master',   DiplomeMasterViewset,    basename='diplome_master')
router.register('note_master',      NoteMasterViewset,       basename='note_master')
router.register('anc_master',       AncienneteMasterViewset, basename='anc_master')
router.register('diplome_licence',  DiplomeLicenceViewset,   basename='diplome_licence')
router.register('note_licence',     NoteLicenceViewset,      basename='note_licence')

router.register('curriculum_vitae', CurvitaeViewset,         basename='curriculum_vitae')
router.register('age',              AgeViewset,              basename='privileges')
router.register('genre',            GenreViewset,            basename='genre')
router.register('letre_motiv',      LettremotivViewset,      basename='letre_motiv')
#____________________End URL_______________________________________________
urlpatterns= router.urls