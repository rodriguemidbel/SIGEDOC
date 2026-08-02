from django.db import models
from params.models import *

# Create your models here.
class Formulaire(models.Model):
    
    detail =       models.CharField(max_length=300)
    repartition =  models.CharField(max_length=300)
    note =         models.CharField(max_length=300)
    commentaire =  models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
            return f"{self.detail}, {self.commentaire}"

class DiplomeMaster(models.Model):
    
    detail =       models.CharField(max_length=500)
    repartition =  models.IntegerField()
    note =         models.IntegerField()
    commentaire =  models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
            return f"{self.detail}, {self.repartition}"

class NoteMaster(models.Model):
    
    detail =       models.CharField(max_length=500)
    repartition =  models.IntegerField()
    note =         models.IntegerField()
    commentaire =  models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
            return f"{self.detail}, {self.repartition}"

class AncienneteMaster(models.Model):
    
    detail =       models.CharField(max_length=500)
    repartition =  models.IntegerField()
    note =         models.IntegerField()
    commentaire =  models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
            return f"{self.detail}, {self.repartition}"
class DiplomeLicence(models.Model):
    
    detail =       models.CharField(max_length=500)
    repartition =  models.IntegerField()
    note =         models.IntegerField()
    commentaire =  models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
            return f"{self.detail}, {self.repartition}"

class NoteLicence(models.Model):
    
    detail =       models.CharField(max_length=500)
    repartition =  models.IntegerField()
    note =         models.IntegerField()
    commentaire =  models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
            return f"{self.detail}, {self.repartition}"
class Curvitae(models.Model):
    
    detail =       models.CharField(max_length=300)
    repartition =  models.CharField(max_length=300)
    note =         models.IntegerField()
    commentaire =  models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
            return f"{self.detail}, {self.commentaire}"

class Age(models.Model):
    
    detail =       models.CharField(max_length=300)
    repartition =  models.CharField(max_length=300)
    note =         models.IntegerField()
    commentaire =  models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
            return f"{self.detail}, {self.commentaire}"

class Genre(models.Model):
    
    detail =       models.CharField(max_length=300)
    repartition =  models.CharField(max_length=300)
    note =         models.IntegerField()
    commentaire =  models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
            return f"{self.detail}, {self.commentaire}"

class Lettremotiv(models.Model):
    
    detail =       models.CharField(max_length=300)
    repartition =  models.CharField(max_length=300)
    note =         models.IntegerField()
    commentaire =  models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
            return f"{self.detail}, {self.commentaire}"