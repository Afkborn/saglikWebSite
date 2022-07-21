

from django.utils.translation import gettext as _
from django.http import HttpResponse
from django.template import loader
# Create your views here.
from .models import *

def index(request):
    web_lang = Language.objects.filter(abbreviated_name=request.LANGUAGE_CODE)[0]
    
    person_list = Person.objects.filter(lang=web_lang.id).order_by('first_name')
    service_list = Service.objects.filter(show_home_screen=True).filter(lang=web_lang.id)
    
    template = loader.get_template('home/index.html')
    
    context = {
        "person_list" : person_list,
        "service_list" : service_list,
    }
    
    return HttpResponse(template.render(context, request))


