from django.forms import ModelForm	
from models import *	
  
class EscriptorForm(ModelForm):	
	class Meta:	
		model =	Escriptor
		exclude = ('user')	

	
  
