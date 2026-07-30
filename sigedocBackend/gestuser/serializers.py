from rest_framework import serializers
from gestuser.models import *



class UsergroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usergroup
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
   
    
    usergroup   = UsergroupSerializer()
    class Meta:
        model = User
        fields = '__all__'

class FeatureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Feature
        fields = '__all__'

class PrivilegeSerializer(serializers.HyperlinkedModelSerializer):

    usergroup = UsergroupSerializer()
    feature = FeatureSerializer()
    class Meta:
        model = Privilege
        fields = '__all__'

class LogSerializer(serializers.HyperlinkedModelSerializer):
    
    user = UserSerializer()
    class Meta:
        model = Log
        fields = '__all__'