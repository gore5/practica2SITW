from django.conf.urls import patterns, include, url
from iTeatre.views import *
from django.views.generic import DetailView, ListView, UpdateView 
from iTeatre.forms import EscriptorForm
from iTeatre.models import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	url(r'^$', mainpage, name='home'),

	url(r'^$', ListView.as_view(context_object_name='contentbody', template_name='iTeatre/llista.html'), name='llista'),

# Create a restaurant, /myrestaurants/restaurants/create/
	url(r'^escriptors/create/$',
		EscriptorCreate.as_view(),
		name='escriptor_create'),
	# Restaurant details, ex.: /myrestaurants/restaurants/1/
	url(r'^escriptors/(?P<pk>\d+)/$',
		EscriptorDetail.as_view(),
		name='escriptor_detail'),

	url(r'^escriptors$', escriptorpagina, name='Llista escriptors'),
	url(r'^escriptors/format=(?P<format>\w+)/$', escriptorpagina, name='Llista escriptors amb format'),
	url(r'^escriptors/(?P<idEscriptor>\d+)/$', escriptordades, name='Dades dels escriptors'),
	url(r'^escriptors/(?P<idEscriptor>\d+)/format=(?P<format>\w+)$', escriptordades, name='Dades dels escriptorsamb format'),

	url(r'^actors$', actorpagina, name='Llista actors'),
	url(r'^actors/format=(?P<format>\w+)/$', actorpagina, name='Llista actors amb format'),
   	url(r'^actors/(?P<idActor>\d+)/$', actordades, name='Dades dels actors'),
	url(r'^actors/(?P<idActor>\d+)/format=(?P<format>\w+)$', actordades, name='Dades dels actors amb format'),

	url(r'^directors$', directorpagina, name='Llista directors'),
	url(r'^directors/format=(?P<format>\w+)/$', directorpagina, name='Llista directors amb format'),
	url(r'^directors/(?P<idDirector>\d+)/$', directordades, name='Dades dels directors'),
	url(r'^directors/(?P<idDirector>\d+)/format=(?P<format>\w+)$', directordades, name='Dades dels directors amb format'),

	url(r'^representacions$', representaciopagina, name='Llista representacions'),
	url(r'^representacions/format=(?P<format>\w+)/$', representaciopagina, name='Llista representacions amb format'),
	url(r'^representacions/(?P<idRepresentacio>\d+)/$', representaciodades, name='Dades de la representacio'),
	url(r'^representacions/(?P<idRepresentacio>\d+)/format=(?P<format>\w+)/$', representaciodades, name='Dades de la representacio amb format'),

	url(r'^obresTeatre$', obra_Teatrepagina, name='Llista obres'),
	url(r'^obresTeatre/format=(?P<format>\w+)/$', obra_Teatrepagina, name='Llista obres teatre amb format'),
	url(r'^obresTeatre/(?P<idObra>\d+)/$', obra_Teatredades, name='Dades de les Obres'),
	url(r'^obresTeatre/(?P<idObra>\d+)/format=(?P<format>\w+)$', obra_Teatredades, name='Dades de les Obres amb format'),

    url(r'^login/$','django.contrib.auth.views.login'),
    #url(r'^Teatre/', include('Teatre.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
