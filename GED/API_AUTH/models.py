from django.db import models

# Create your models here.
class Profils(models.Model):
    code_utilisateur = models.CharField(max_length=50,default='')
    nom_utilisateur  = models.CharField(max_length = 30,default='')
    
    
    
    
    
class Utilisateurs(models.Model):
    code = models.CharField(max_length=50,default='')
    nom  = models.CharField(max_length = 30,default='')
    motdepasse = models.CharField(max_length = 30,default='')
    