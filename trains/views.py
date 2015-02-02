from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core import serializers
import json
from trains.models import *
# Create your views here.

# @csrf_exempt
def stations_list_ajax(request):
    data = serializers.serialize("json", Stations.objects.all())
    data = {'count': 0,
            'stations': [{'code': 's100', 'order': 7, 'name': 'выхино'},{'code': 's100', 'order': 7, 'name': 'выхино'}]}
    return HttpResponse(json.dumps(data), content_type='application/json')


def stations_list_ajax_my(request):
    data = {'count': 0,
            'stations': [{'code': 's100', 'order': 7, 'name': 'выхино'},{'code': 's100', 'order': 7, 'name': 'выхино'}]}
    # for station in Stations.objects.all():
    # return HttpResponse(json.dumps(data), content_type='application/json')
    return  render_to_response("trains/autocomplete.html")