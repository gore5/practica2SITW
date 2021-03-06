from django.db import models
from django.contrib.auth.models import User
from datetime import *
from django.core.urlresolvers import reverse


# Create your models here.


class Person(models.Model):
	nom = models.CharField(max_length=40)
	edat = models.IntegerField()
	sexe = models.CharField(max_length=1)
	localitat = models.CharField(max_length=40)


class Escriptor(Person):
	user = models.ForeignKey(User, blank=True,null=True)	
  

	def __unicode__(self):
		return self.nom

	def get_absolute_url(self):
		return reverse('escriptor_detail',kwargs={'pk':self.pk})

  
class Actor(Person):
	user = models.ForeignKey(User,blank=True,null=True)	
	
	def __unicode__(self):
	        return self.nom

	def get_absolute_url(self):
        	return reverse('actor_detail', kwargs={'pk': self.pk})




class Director(Person):
	user = models.ForeignKey(User,blank=True,null=True)	

	def __unicode__(self):
		return self.nom

	def get_absolute_url(self):
        	return reverse('director_detail', kwargs={'pk': self.pk})




class nom_Obra (models.Model):
	nomObra = models.CharField(null=False,max_length=40)
	user = models.ForeignKey(User,blank=True,null=True)	

	def __unicode__(self):
		return self.nomObra

	def get_absolute_url(self):
        	return reverse('nom_obra_detail', kwargs={'pk': self.pk})
	

class Representacio (models.Model):
	nomRepresentacio = models.CharField(max_length=40)
	nomObra = models.ForeignKey(nom_Obra)
	dataInici = models.DateField()
	dataFi = models.DateField()
	actors = models.ManyToManyField(Actor)
	director = models.ForeignKey(Director)
	user = models.ForeignKey(User,blank=True,null=True)	
	
	

	def __unicode__(self):
		return self.nom
	def get_absolute_url(self):
        	return reverse('representacio_detail', kwargs={'pk1': self.nomObra.pk,'pkr2':self.director.pk,'pkr3':self.actors.pk, 'pk': self.pk})


class Obra_Teatre(models.Model):
	nom = models.ForeignKey(nom_Obra)
	Tipus = models.CharField(max_length=40)
	escriptor = models.ForeignKey(Escriptor)
	representacions = models.ManyToManyField(Representacio)
	user = models.ForeignKey(User,blank=True,null=True)	

	def __unicode__(self):
		return self.nom.nomObra

	def get_absolute_url(self):
        	return reverse('obra_Teatre_detail', kwargs={'pkr1': self.nom.pk,'pkr2':self.escriptor.pk, 'pkr3': self.representacions.pk, 'pk': self.pk})




