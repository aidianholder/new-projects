from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json

from .models import Facility, Inspection


def index(request):
    return HttpResponse("index page goes here.  build an index page aidian")


def facility_by_name(request, name_string):
    name_string_clean = name_string.upper().strip()
    facilities = Facility.objects.filter(facilty_name__startswith=name_string_clean)







