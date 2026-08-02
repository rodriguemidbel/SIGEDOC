"""
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from sigedocBackend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/params/', include('params.routers')),
    path('api/gestuser/', include('gestuser.routers')),
    #--------------
    path('api/gestuser/connect_user',    views.connect_user,    name='connect_user'),
    path('api/gestuser/deconnect_user',  views.deconnect_user,  name='deconnect_user'),
    path('api/gestuser/change_password', views.change_password, name='change_password'),
    path('api/gestuser/forget_password', views.forget_password, name='forget_password'),
]
