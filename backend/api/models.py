from __future__ import unicode_literals

from django.db import models
from django.core.validators import *

from django.contrib.auth.models import User, Group

from django.contrib import admin
import base64

class Event(models.Model):
    eventtype = models.CharField(max_length=1000, blank=False)
    timestamp = models.DateTimeField()
    userid = models.CharField(max_length=1000, blank=True)
    requestor = models.GenericIPAddressField(blank=False)

    def __str__(self):
        return str(self.eventtype)

class EventAdmin(admin.ModelAdmin):
    list_display = ('eventtype', 'timestamp')

class ApiKey(models.Model):
    owner = models.CharField(max_length=1000, blank=False)
    key = models.CharField(max_length=5000, blank=False)

    def __str__(self):
        return str(self.owner) + str(self.key)

class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ('owner','key')

class Dog(models.Model):
    name = models.CharField(max_length=1000, blank=False)
    age = models.IntegerField(validators=[MinValueValidator(0)], blank=False, null=True)
    gender = models.CharField(max_length=1000, blank=False, null=True)
    color = models.CharField(max_length=1000, blank=False, null=True)
    favoritefood = models.CharField(max_length=1000, blank=False, null=True)
    favoritetoy = models.CharField(max_length=1000, blank=False, null=True)
	
    def __str__(self):
        return str(self.name) + ", " + str(self.age)
        
class Breed(models.Model):
    name = models.CharField(max_length=1000, blank=False)
    #Don't forget to add validators for Small, Medium, and Large
    size = models.CharField(max_length=1000, blank=False)
    friendliness = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], blank=False, null=True)
    trainability = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], blank=False, null=True)
    sheddingamount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], blank=False, null=True)
    exerciseneeds = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], blank=False, null=True)
    
    def __str__(self):
        return str(self.name) + ", " + str(self.size)