from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def ip(request):
    return HttpResponse('THIS IS IP ADDRESS PROJECT')