from django.shortcuts import render
from django.http import HttpResponse
from models import Heard


def listen(request):
    h = Heard(payload=request.body)
    h.save()
    hub_token = request.GET.get('hub.challenge')
    return HttpResponse(hub_token)
