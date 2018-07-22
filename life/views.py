from django.shortcuts import render
from django.core import serializers

def index(request):
    return render(request, 'life/index.html')
  
def detail(request, user_name):
    return HttpResponse("You're looking at users %s." % user_name)