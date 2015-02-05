from django.shortcuts import render
from django.http import HttpResponse
from models import Heard


def listen(request):
    h = Heard(payload=request.POST)
    h.save()
    return HttpResponse(request.POST)
