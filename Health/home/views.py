

from django.utils.translation import gettext as _
from django.http import HttpResponse
from django.template import loader
# Create your views here.
from .models import *

def index(request):
    person_list = Person.objects.order_by('first_name')
    template = loader.get_template('home/index.html')
    context = {
        "person_list" : person_list
    }
    
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)