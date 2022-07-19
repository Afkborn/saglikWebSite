
from django.shortcuts import render
from django.utils.translation import gettext as _
# from django.http import HttpResponse
# Create your views here.

def index(request):

    return render(request,"home/index.html")