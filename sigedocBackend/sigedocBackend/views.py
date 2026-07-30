# API permettant la connexion au système
from MySQLdb import IntegrityError
from gestuser.serializers import *
from gestuser.models import User, Log
from rest_framework.response import Response
from rest_framework          import status
from rest_framework.decorators import api_view
from django.utils import timezone
from django.utils.crypto import get_random_string


@api_view(['POST'])
def connect_user(request, *args, **kwargs):

    resp_options = []
    
    loginUser = request.data.get('username')
    mdpUser = request.data.get('password')
    print(f"username : {loginUser}")
    print(f"password : {mdpUser}")
      
    if not loginUser or not mdpUser:
        resp_options = {
            "message": "Veuillez indiquer votre nom d'utilisateur et votre mot de passe.",
            "status": status.HTTP_401_UNAUTHORIZED,
            "data": []
        }
        return Response(resp_options)
    
    utilisateur = User.objects.get(loginUser=loginUser,mdpUser=mdpUser)
    
    if utilisateur:
        serializer = UserSerializer(utilisateur)
        resp_options = {
            "message": "Données disponible",
            "status": status.HTTP_200_OK,
            "data": serializer.data
        }
        #----------
        #Renseignement de la table historique des actions
        try:
            tmp = Log(user=utilisateur,action="Connection au système")
            tmp.save()
        except IntegrityError as e:
            # Catch specific database-related errors like unique constraint violations
            print(f"Database integrity error: {e}")
        except ValueError as e:
            # Catch errors related to invalid data types or values
            print(f"Value error during save: {e}")
        except Exception as e:
            # Catch any other unexpected exceptions
            print(f"An unexpected error occurred during save: {e}")
        #-----------
        #Mise a jour du statut de connection de l'utilisateur
        try:
            us = User.objects.get(pk=resp_options["data"]["id"])
            us.is_active = True
            us.last_login_at = timezone.now()
            us.save()
        except IntegrityError as e:
            # Catch specific database-related errors like unique constraint violations
            print(f"Database integrity error: {e}")
        except ValueError as e:
            # Catch errors related to invalid data types or values
            print(f"Value error during save: {e}")
        except Exception as e:
            # Catch any other unexpected exceptions
            print(f"An unexpected error occurred during save: {e}")
        #-------------------
        return Response(resp_options)
    else:
        resp_options = {
            "message": "Données indisponible, Username et Password invalide",
            "status": status.HTTP_404_NOT_FOUND,
            "data": []
        }
        return Response(resp_options)
    

# API permettant la deconnexion au système
@api_view(['POST'])
def deconnect_user(request, *args, **kwargs):

    resp_options = []
    
    loginUser = request.query_params.get('username',None)
    
    if not loginUser :
        resp_options = {
            "message": "Veuillez indiquer votre nom d'utilisateur",
            "status": status.HTTP_401_UNAUTHORIZED,
            "data": []
        }
        return Response(resp_options)
    
    utilisateur = User.objects.get(loginUser=loginUser)
    
    if utilisateur:
        serializer = UserSerializer(utilisateur)
        resp_options = {
            "message": "Vous étes déconnectez du systène",
            "status": status.HTTP_200_OK,
            "data": serializer.data
        }
        #----------
        #Renseignement de la table historique des actions
        try:
            tmp = Log(user=utilisateur,action="Vous ètes deconnecter du système")
            tmp.save()
        except IntegrityError as e:
            # Catch specific database-related errors like unique constraint violations
            print(f"Database integrity error: {e}")
        except ValueError as e:
            # Catch errors related to invalid data types or values
            print(f"Value error during save: {e}")
        except Exception as e:
            # Catch any other unexpected exceptions
            print(f"An unexpected error occurred during save: {e}")
        #-----------
        #Mise a jour du statut de connection de l'utilisateur
        try:
            us = User.objects.get(pk=resp_options["data"]["id"])
            us.is_active = False
            us.save()
        except IntegrityError as e:
            # Catch specific database-related errors like unique constraint violations
            print(f"Database integrity error: {e}")
        except ValueError as e:
            # Catch errors related to invalid data types or values
            print(f"Value error during save: {e}")
        except Exception as e:
            # Catch any other unexpected exceptions
            print(f"An unexpected error occurred during save: {e}")
        #-------------------
        return Response(resp_options)
    else:
        resp_options = {
            "message": "Données indisponible, Username et Password invalide",
            "status": status.HTTP_404_NOT_FOUND,
            "data": []
        }
        return Response(resp_options)
    

@api_view(['POST'])
def change_password(request, *args, **kwargs):

    resp_options = []
   
    mdpUser = request.query_params.get('password',None)
    new_mdpUser = request.query_params.get('new_password',None)

      
    if not mdpUser:
        resp_options = {
            "message": "Veuillez indiquer votre mot de passe.",
            "status": status.HTTP_401_UNAUTHORIZED,
            "data": []
        }
        return Response(resp_options)
    
    utilisateur = User.objects.get(mdpUser=mdpUser)
    
    if utilisateur:
        serializer = UserSerializer(utilisateur)
        resp_options = {
            "message": "Données disponible",
            "status": status.HTTP_200_OK,
            "data": serializer.data
        }
        #----------
        #Renseignement de la table historique des actions
        try:
            tmp = Log(user=utilisateur,action="Changement du mot de passe")
            tmp.save()
        except IntegrityError as e:
            # Catch specific database-related errors like unique constraint violations
            print(f"Database integrity error: {e}")
        except ValueError as e:
            # Catch errors related to invalid data types or values
            print(f"Value error during save: {e}")
        except Exception as e:
            # Catch any other unexpected exceptions
            print(f"An unexpected error occurred during save: {e}")
        #-----------
        #Mise a jour du mot de passe de l'utilisateur
        try:
            us = User.objects.get(pk=resp_options["data"]["id"])
            us.mdpUser = new_mdpUser
            us.save()
        except IntegrityError as e:
            # Catch specific database-related errors like unique constraint violations
            print(f"Database integrity error: {e}")
        except ValueError as e:
            # Catch errors related to invalid data types or values
            print(f"Value error during save: {e}")
        except Exception as e:
            # Catch any other unexpected exceptions
            print(f"An unexpected error occurred during save: {e}")
        #-------------------
        return Response(resp_options)
    else:
        resp_options = {
            "message": "Données indisponible, Password invalide",
            "status": status.HTTP_404_NOT_FOUND,
            "data": []
        }
        return Response(resp_options)

@api_view(['POST'])
def forget_password(request, *args, **kwargs):

    resp_options = []
   
    email = request.query_params.get('email',None)
      
    if not email:
        resp_options = {
            "message": "Veuillez indiquer votre mot de passe.",
            "status": status.HTTP_401_UNAUTHORIZED,
            "data": []
        }
        return Response(resp_options)
    
    utilisateur = User.objects.get(email=email)
    
    if utilisateur:
        serializer = UserSerializer(utilisateur)
        resp_options = {
            "message": "Données disponible",
            "status": status.HTTP_200_OK,
            "data": serializer.data
        }
        #----------
        #Renseignement de la table historique des actions
        try:
            tmp = Log(user=utilisateur,action="Régéneration du mot de passe")
            tmp.save()
        except IntegrityError as e:
            # Catch specific database-related errors like unique constraint violations
            print(f"Database integrity error: {e}")
        except ValueError as e:
            # Catch errors related to invalid data types or values
            print(f"Value error during save: {e}")
        except Exception as e:
            # Catch any other unexpected exceptions
            print(f"An unexpected error occurred during save: {e}")
        #-----------
        #Mise a jour du mot de passe de l'utilisateur
        try:
            # Generate a random alphanumeric string of length 10
            random_string = get_random_string(10)

            us = User.objects.get(pk=resp_options["data"]["id"])
            us.mdpUser = random_string
            us.save()
        except IntegrityError as e:
            # Catch specific database-related errors like unique constraint violations
            print(f"Database integrity error: {e}")
        except ValueError as e:
            # Catch errors related to invalid data types or values
            print(f"Value error during save: {e}")
        except Exception as e:
            # Catch any other unexpected exceptions
            print(f"An unexpected error occurred during save: {e}")
        #-------------------
        return Response(resp_options)
    else:
        resp_options = {
            "message": "Données indisponible, Password invalide",
            "status": status.HTTP_404_NOT_FOUND,
            "data": []
        }
        return Response(resp_options)

    
