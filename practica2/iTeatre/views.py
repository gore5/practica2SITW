#-*- coding: utf-8 -*-

from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from models import *



def mainpage(request):

	template = get_template('index.html')
	variables = Context({
		'titlehead': 'Teatre aPP',
		'pagetitle': 'Benvingut a la aplicació de Teatres',
		'contentbody': 'Aquí podràs administrar coses de Teatre',
		'user': request.user,
	})
	output = template.render(variables)
	return HttpResponse(output)


#--------------------------------------------ESCRIPTOR------------------------------------------------

def escriptorpagina(request, format='html'):

	escriptor = Escriptor.objects.all()
	if(format=='xml'):
		template = get_template('llista.xml')
	else:
		template = get_template('llista.html')
	variables = Context({
		'pagetitle': "Llista d'escriptors",
		'contentbody': escriptor,
		'name':'/escriptors/',
		'tag1':'escriptors',
		'tag2':'escriptor',
		'user': request.user,
	})
	output = template.render(variables)
	return HttpResponse(output)

def escriptordades(request, idEscriptor, format='html'):

	escriptor = Escriptor.objects.get(id=idEscriptor)
	if(format=='xml'):
		template = get_template('dades.xml')
	else:
		template = get_template('dades.html')
	variables = Context({
		'pagetitle': 'Dades del escriptor',
		'contentbody': escriptor,
		'tag1':'escriptors',
		'tag2':'escriptor',
		'user': request.user,
	})
	output = template.render(variables)
	return HttpResponse(output)


#----------------------------------------------ACTOR--------------------------------------------------

def actorpagina(request, format='html'):

	actor = Actor.objects.all()
	if(format=='xml'):
		template = get_template('llista.xml')
	else:
		template = get_template('llista.html')
	variables = Context({
		'pagetitle': "Llista d'actors",
		'contentbody': actor,
		'name':'/actors/',
		'tag1':'actors',
		'tag2':'actor',
		'user': request.user,
	})
	output = template.render(variables)
	return HttpResponse(output)

def actordades(request, idActor, format='html'):

	actor = Actor.objects.get(id=idActor)
	if(format=='xml'):
		template = get_template('dades.xml')
	else:
		template = get_template('dades.html')
	variables = Context({
		'pagetitle': 'Dades del actor',
		'contentbody': actor,
		'tag1':'actors',
		'tag2':'actor',
		'user': request.user,
	})
	output = template.render(variables)
	return HttpResponse(output)


#--------------------------------------------DIRECTOR------------------------------------------------

def directorpagina(request, format='html'):

	director = Director.objects.all()
	if(format=='xml'):
		template = get_template('llista.xml')
	else:
		template = get_template('llista.html')
	variables = Context({
		'pagetitle': 'Llista de Directors',
		'contentbody': director,
		'name':'/directors/',
		'tag1':'directors',
		'tag2':'director',
		'user': request.user,
	})
	output = template.render(variables)
	return HttpResponse(output)

def directordades(request, idDirector, format='html'):

	director = Director.objects.get(id=idDirector)
	if(format=='xml'):
		template = get_template('dades.xml')
	else:
		template = get_template('dades.html')
	variables = Context({
		'pagetitle': 'Dades del director',
		'contentbody': director,
		'tag1':'directors',
		'tag2':'director',
		'user': request.user,
	})
	output = template.render(variables)
	return HttpResponse(output)


#--------------------------------------------REPRESENTACIO------------------------------------------------

def representaciopagina(request, format='html'):

	representacio = Representacio.objects.all()
	if(format=='xml'):
		template = get_template('llista.xml')
	else:
		template = get_template('llista.html')
	variables = Context({
		'pagetitle': 'Llista de Representacions',
		'contentbody': representacio,
		'name':'/representacions/',
		'tag1':'representacions',
		'user': request.user,
	})
	output = template.render(variables)
	return HttpResponse(output)


def representaciodades(request, idRepresentacio, format='html'):

	representacio = Representacio.objects.get(id=idRepresentacio)
	if(format=='xml'):
		template = get_template('representacio.xml')
	else:
		template = get_template('representacio.html')
	variables = Context({
		'pagetitle': 'Informació de la representació',
		'contentbody': representacio,
		'tag1':'representacions',
		'user': request.user,
	})
	output = template.render(variables)
	return HttpResponse(output)
#-------------------------------------------------OBRA-----------------------------------------------------

def obra_Teatrepagina(request, format='html'):

	obra_Teatre = Obra_Teatre.objects.all()
	if(format=='xml'):
		template = get_template('llista.xml')
	else:
		template = get_template('llista.html')
	variables = Context({
		'pagetitle': "Llista d'obres de teatre",
		'contentbody': obra_Teatre,
		'name':'/obresTeatre/',
		'tag1':'obresTeatre',
		'user': request.user,
	})
	output = template.render(variables)
	return HttpResponse(output)


def obra_Teatredades(request, idObra, format='html'):

	obra_Teatre  = Obra_Teatre.objects.get(id=idObra)
	if(format=='xml'):
		template = get_template('Obrateatre.xml')
	else:
		template = get_template('infoObresTeatre.html')
	variables = Context({
		'pagetitle': 'Informació de les obres de teatre',
		'contentbody': obra_Teatre,
		'tag1':'obresTeatre',
		'user': request.user,
	})
	output = template.render(variables)
	return HttpResponse(output)







