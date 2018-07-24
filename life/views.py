from django.shortcuts import render
from django.core import serializers
from .models import User
from .models import Meeting
import json

def index(request):
    content = {"users": User.objects.all(), "meetings": Meeting.objects.all()}
    return render(request, 'life/index.html', content)
  
def signup(request):
  if request.method == "POST":
    print(request.body)
    body = json.loads(request.body.decode('utf-8'))
    print(body)
    #json.loads(request.body.decode('utf-8')) 
    print ("body", body)
    newUser = User(name=body['name'], password=body['password'], email=body['email'])
    newUser.save()
  content = {"users": User.objects.all()}
  return render(request, 'life/signup.html', content)
  
def signin(request):
  if request.method == "POST":
    print (request.body)
    body = json.loads(request.body.decode('utf-8')) 
    print ("body", body)
    
    x = User.objects.filter(email=body['email'] ).get(password=body['password'])
    print (x)
#     if x:
#       return window.location.replace("life/welcome/" + body.email)
  else:
    content = {"users": User.objects.all()}
    return render(request, 'life/signin.html', content)
  
def welcome(request, personInfo):
  content = {person: User.objects.get(email=personInfo)}
  return render(request, content)

def addMeeting(request, personInfo):
  if request.method == "POST":
    body = request.body
    print (body)
    p = []
    for l in body.participants:
      p.push(User.objects.get(email=l))
    x = Meeting(name=body.name, description=body.description, participants = p)
    x.save()
  else:
    return render(request, 'life/meet.html')
 
def addTask(request):
  if request.method == "POST":
    body = request.body
    print (body)
    x = Meeting(name=body.name, description=body.description)
    x.save()
  else:
    return render(request, 'life/addtask.html')
  
def addFriend(request):
  body = request.body
  x = User.objects.get(email=body.email)
  adding = User.objects.get(email=body.friendemail)
  x.add(adding)
  
def friends(request):
  return render(request, 'life/friends.html')
 
def schedule(request):
  if request.method == "POST":
    body = request.body
    
  else:
    return render(request, 'life/schedule.html')
  
def detail(request, user_email):
    context = {'User': user_email}
    return render(request, 'life/index.html', context) 