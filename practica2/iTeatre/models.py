from django.db import models
from django.contrib.auth.models import User
from datetime import *
from django.core.urlresolvers import reverse


# Create your models here.


class Escriptor(models.Model):
	nom = models.CharField(max_length=40)
	edat = models.IntegerField()
	sexe = models.CharField(max_length=1)
	localitat = models.CharField(max_length=40)
	user = models.ForeignKey(User, blank=True,null=True)	
  

	def __unicode__(self):
		return self.nom

	def get_absolute_url(self):
		return reverse('escriptor_detail',kwargs={'pk':self.pk})



class Actor(models.Model):
	nom = models.CharField(max_length=40)
	edat = models.IntegerField()
	sexe = models.CharField(max_length=1)
	localitat = models.CharField(max_length=40)
	user = models.ForeignKey(User,blank=True,null=True)	
	
	def __unicode__(self):
	        return self.nom


class Director(models.Model):
	nom = models.CharField(max_length=40)
	edat = models.IntegerField()
	sexe = models.CharField(max_length=1)
	localitat = models.CharField(max_length=40)
	user = models.ForeignKey(User,blank=True,null=True)	

	def __unicode__(self):
		return self.nom


class nom_Obra (models.Model):
	nomObra = models.CharField(primary_key=True,max_length=40)
	user = models.ForeignKey(User,blank=True,null=True)	

	def __unicode__(self):
		return self.nomObra
	

class Representacio (models.Model):
	nom = models.CharField(max_length=40)
	nomObra = models.ForeignKey(nom_Obra)
	dataInici = models.DateField()
	dataFi = models.DateField()
	actors = models.ManyToManyField(Actor)
	director = models.ForeignKey(Director)
	user = models.ForeignKey(User,blank=True,null=True)	
	
	

	def __unicode__(self):
		return self.nom


class Obra_Teatre(models.Model):
	nom = models.ForeignKey(nom_Obra)
	Tipus = models.CharField(max_length=40)
	escriptor = models.ForeignKey(Escriptor)
	representacions = models.ManyToManyField(Representacio)
	user = models.ForeignKey(User,blank=True,null=True)	

	def __unicode__(self):
		return self.nom.nomObra




