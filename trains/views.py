from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core import serializers
import json
from django.shortcuts import render
from trains.models import *
# Create your views here.
def stations_list_ajax(request):
    data = serializers.serialize("json", Stations.objects.all())
    return HttpResponse(json.dumps(data), content_type='application/json')

    pass