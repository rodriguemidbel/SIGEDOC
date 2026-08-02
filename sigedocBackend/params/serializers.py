from rest_framework import serializers
from params.models import *


class FormulaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formulaire
        fields = '__all__'

class DiplomeMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiplomeMaster
        fields = '__all__'

class NoteMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteMaster
        fields = '__all__'

class AncienneteMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AncienneteMaster
        fields = '__all__'

class DiplomeLicenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiplomeLicence
        fields = '__all__'

class NoteLicenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteLicence
        fields = '__all__'
        
class CurvitaeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curvitae
        fields = '__all__'

class AgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Age
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class LettremotivSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lettremotiv
        fields = '__all__'

