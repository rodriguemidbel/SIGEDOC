from django.db import models
from params.models import *
# Create your models here.
def upload_path(instance, filename):
    return '/'.join(['photos-profil', filename])

class Usergroup(models.Model):
    
    group_name = models.CharField(max_length=300)
    group_desc = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
            return f"{self.group_name}, {self.group_desc}"

class User(models.Model):
    title             = models.CharField(max_length=10,blank=True,null=True)
    first_name        = models.TextField(blank=True, null=True)
    last_name         = models.TextField(blank=True, null=True)
    pays              = models.TextField(blank=True, null=True)
    phone             = models.TextField(blank=True, null=True)
    email             = models.TextField(blank=True, null=True)
    address           = models.TextField(blank=True, null=True)
    job               = models.TextField(blank=True,null=True)
    usergroup         = models.ForeignKey('Usergroup', blank=True, null=True, related_name='usergroups', on_delete=models.CASCADE)
    loginUser         = models.TextField(blank=True, null=True)
    mdpUser           = models.TextField(blank=True, null=True)
    profile_photo_url = models.FileField(upload_to=upload_path, blank=True, null=True)
    status            = models.CharField(blank=True,null=True,max_length=255)
    is_active         = models.BooleanField(default=False,blank=True)
    last_login_at     = models.DateTimeField(blank=True, null=True)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    created_at        = models.DateTimeField(auto_now_add=True)
    updated_at        = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"

class Feature(models.Model):

    nom_feat = models.CharField(max_length=255)
    desc_feat = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nomFct
    
class Privilege(models.Model):

    usergroup  =   models.ForeignKey('Usergroup', blank=True, null=True, related_name='usergroups_priv', on_delete=models.CASCADE)
    feature =      models.ForeignKey('Feature',      blank=True, null=True, related_name='features_priv', on_delete=models.CASCADE)
    create =       models.BooleanField(null=True, default=False)
    read =         models.BooleanField(null=True, default=False)
    update =       models.BooleanField(null=True, default=False)
    delete =       models.BooleanField(null=True, default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.usergroup}, {self.feature}, {self.create}, {self.read}, {self.update}, {self.delete}"

class Log(models.Model):

    user = models.ForeignKey('User', blank=True, null=True, related_name='users_log', on_delete=models.CASCADE)
    action = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user