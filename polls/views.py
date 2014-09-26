# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, Http404
from django.template import Context,loader
from polls.models import Poll


def index(request):
    return render(request,'polls/index.html', {'latest_poll_list': Poll.objects.order_by('-pub_date')[:5]})

def detail(request, poll_id):
    return render(request, 'polls/detail.html', {'poll': get_object_or_404(Poll, pk=poll_id)})




def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)


def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)