
from django.http import Http404
from django.utils.translation import gettext as _
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import *


def index(request):
    try:
        web_lang = Language.objects.filter(abbreviated_name=request.LANGUAGE_CODE)[0]
    except:
        get_default_lang()
        web_lang = Language.objects.filter(abbreviated_name=request.LANGUAGE_CODE)[0]
    home_screen_slide_list = HomeScreenSlide.objects.filter(lang=web_lang.id)
    person_list = Person.objects.filter(lang=web_lang.id).order_by('first_name')
    service_list = Service.objects.filter(show_home_screen=True).filter(lang=web_lang.id)
    comment_list = Comment.objects.all
    if (service_list.count() > 6):
        service_list = service_list.order_by('?')
        service_list = service_list[:6]
        
    template = loader.get_template('home/index.html')
    context = {
        "home_screen_slide_list" : home_screen_slide_list,
        "service_list" : service_list,
        "person_list" : person_list,
        "comment_list" : comment_list,
    }
    
    return HttpResponse(template.render(context, request))


def services(request, service_id):
    try:
        web_lang = Language.objects.filter(abbreviated_name=request.LANGUAGE_CODE)[0]
    except:
        get_default_lang()
        web_lang = Language.objects.filter(abbreviated_name=request.LANGUAGE_CODE)[0]
    try:
       service = get_object_or_404(Service, pk=service_id)
       service_list = Service.objects.filter(lang=web_lang.id)
       template = loader.get_template('home/services.html')
       context = {
           "service" : service,
           "service_list" : service_list
        }
    except Service.DoesNotExist:
        raise Http404("Service does not exist")
    return HttpResponse(template.render(context, request))


def servicesHome(request):
    try:
        web_lang = Language.objects.filter(abbreviated_name=request.LANGUAGE_CODE)[0]
    except:
        get_default_lang()
        web_lang = Language.objects.filter(abbreviated_name=request.LANGUAGE_CODE)[0]
    try:
       service_list = Service.objects.filter(lang=web_lang.id)
       template = loader.get_template('home/services.html')
       context = {
           "service_list" : service_list
        }
    except Service.DoesNotExist:
        raise Http404("Service does not exist")
    return HttpResponse(template.render(context, request))

