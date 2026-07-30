from MySQLdb import IntegrityError
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from gestuser.serializers import *
from gestuser.models import User, Log
from rest_framework.response import Response
from rest_framework          import status
from rest_framework.decorators import api_view
from django.utils import timezone

from django.contrib.auth import authenticate
from rest_framework.serializers import ModelSerializer
# Create your views here.
   
class UsergroupViewset(ModelViewSet):

    serializer_class = UsergroupSerializer
    
    
    def get_queryset(self):
        return Usergroup.objects.all()

    def create(self, request, *args, **kwargs):
        group_name = request.data["group_name"]
        group_desc = request.data["group_desc"]
       
        Usergroup.objects.create(group_name = group_name,group_desc =group_desc)
        return Response("Enregistrement effectué avec succés", status = status.HTTP_200_OK)

class UserViewset(ModelViewSet):

    serializer_class = UserSerializer
    
    def get_queryset(self):

        return User.objects.all()
        

    def create(self, request, *args, **kwargs):
            
            title = request.data["title"]
            first_name = request.data["first_name"]
            last_name = request.data["last_name"]
            pays = request.data["pays"]
            phone = request.data["phone"]
            email = request.data["email"]
            address = request.data["address"]
            job = request.data["job"]
            usergroup = request.data["usergroup"]
            loginUser = request.data["loginUser"]
            mdpUser = request.data["mdpUser"]
            profile_photo_url = request.data["profile_photo_url"]
            status = request.data["status"]
            is_active = request.data["is_active"]
            last_login_at = request.data["last_login_at"]
            email_verified_at = request.data["email_verified_at"]
        
            User.objects.create(title = title,
                            first_name = first_name,
                            last_name = last_name,
                            pays = pays,
                            phone = phone,
                            email = email,
                            address = address,
                            job    = job,
                            usergroup = Usergroup.objects.get(id = int(usergroup)),
                            loginUser = loginUser,
                            mdpUser = mdpUser,
                            profile_photo_url = profile_photo_url,
                            status = status,
                            is_active = is_active,
                            last_login_at = last_login_at,
                            email_verified_at = email_verified_at
                            )
            return Response("Enregistrement effectué avec succés", status = status.HTTP_200_OK)

class LogViewset(ModelViewSet):

    queryset = Log.objects.all()
    serializer_class = LogSerializer

    def create(self, request, *args, **kwargs):
        user = request.data["user"]
        action = request.data["action"]


        Log.objects.create(user = User.objects.get(id = int(user)),
                           action = action
                          )
        return Response("Enregistrement effectué avec succés", status = status.HTTP_200_OK)

#---
class FeatureViewset(ModelViewSet):

    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer

    def create(self, request, *args, **kwargs):
        nom_feat = request.data["nom_feat"]
        desc_feat = request.data["desc_feat"]


        Feature.objects.create(nom_feat = nom_feat,
                                desc_feat = desc_feat
                                    )
        return Response("Enregistrement effectué avec succés", status = status.HTTP_200_OK)
    
#---    
class PrivilegeViewset(ModelViewSet):

    queryset = Privilege.objects.all()
    serializer_class = PrivilegeSerializer

    def create(self, request, *args, **kwargs):
        usergroup = request.data["usergroup"]
        feature = request.data["feature"]
        create = request.data["create"]
        read = request.data["read"]
        update = request.data["update"]
        delete = request.data["delete"]

        Privilege.objects.create(usergroup = Usergroup.objects.get(id = int(usergroup)),
                                feature = Feature.objects.get(id = int(feature)),
                                create = create,
                                read = read,
                                update = update,
                                delete = delete
                          )
        return Response("Enregistrement effectué avec succés", status = status.HTTP_200_OK)

