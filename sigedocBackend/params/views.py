from MySQLdb import IntegrityError
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from params.serializers import *
from params.models import *
from rest_framework.response import Response
from rest_framework          import status
from rest_framework.decorators import api_view
from django.utils import timezone

from django.contrib.auth import authenticate
from rest_framework.serializers import ModelSerializer

# Create your views here.
class FormulaireViewset(ModelViewSet):
    serializer_class = FormulaireSerializer
    def get_queryset(self):
        return Formulaire.objects.all()
class DiplomeMasterViewset(ModelViewSet):
    serializer_class = DiplomeMasterSerializer
    def get_queryset(self):
        return DiplomeMaster.objects.all()
class NoteMasterViewset(ModelViewSet):
    serializer_class = NoteMasterSerializer
    def get_queryset(self):
        return NoteMaster.objects.all()
class AncienneteMasterViewset(ModelViewSet):
    serializer_class = AncienneteMasterSerializer
    def get_queryset(self):
        return AncienneteMaster.objects.all()

class DiplomeLicenceViewset(ModelViewSet):
    serializer_class = DiplomeLicenceSerializer
    def get_queryset(self):
        return DiplomeLicence.objects.all()
class NoteLicenceViewset(ModelViewSet):
    serializer_class = NoteLicenceSerializer
    def get_queryset(self):
        return NoteLicence.objects.all()

class CurvitaeViewset(ModelViewSet):
    serializer_class = CurvitaeSerializer
    def get_queryset(self):
        return Curvitae.objects.all()
    
class AgeViewset(ModelViewSet):
    serializer_class = AgeSerializer
    def get_queryset(self):
        return Age.objects.all()
    
class GenreViewset(ModelViewSet):
    serializer_class = GenreSerializer
    def get_queryset(self):
        return Genre.objects.all()
class LettremotivViewset(ModelViewSet):
    serializer_class = LettremotivSerializer
    def get_queryset(self):
        return Lettremotiv.objects.all()
