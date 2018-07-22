from django.db import models

class User(models.Model):
  name = models.CharField(max_length=50)
  email = models.EmailField()
  password = models.CharField(max_length=50)
  friends = models.ManyToManyField("self", blank=True)
 # timesFree = models.ArrayModelField(models.IntegerField(),size=24,)
 
class Meeting(models.Model):
  name = models.CharField(max_length=50)
  description = models.TextField(max_length=200)
  participants = models.ManyToManyField('User')
  
# class Group(models.Model):
# 	established = models.DateTimeField(auto_now_add=True)
# 	name = models.CharField(max_length=50)
#   timesFree = ArrayField(models.IntegerField(),size=24,)
  
# class Activity(models.Model):
#   groupWith = models.ForeignKey(Group, on_delete=models.CASCADE)
#   name = models.CharField(max_length=50)
#   calories = models.IntegerField(default=0)
#   description = models.TextField(max_length=200)