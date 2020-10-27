from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
import datetime

class Activation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)


class User_Attributes(models.Model):
    date = models.DateTimeField()
    user = models.IntegerField()
    details_filled = models.BooleanField()
    age = models.IntegerField()
    pneumonia = models.BooleanField()
    gender = models.CharField(max_length=10)
    obesity = models.BooleanField()
    breathing = models.BooleanField()
    pregnant = models.BooleanField()
    smoker = models.BooleanField()
    diabetic = models.BooleanField()
    ckd = models.BooleanField()
    copd = models.BooleanField()
    immunocompromised = models.BooleanField()
    heart = models.BooleanField()
    asthma = models.BooleanField()
    blood = models.BooleanField()
    others = models.BooleanField()


class Request_Manager(models.Manager):
    def create_data(self, user,hospital,priority,fulfilled,confirmtime):
        details = self.create(user=user,hospital=hospital,time=datetime.datetime.now(),priority=priority,fulfilled=fulfilled,confirmtime=confirmtime)
        return details

class Request(models.Model):
    user = models.IntegerField()
    hospital = models.IntegerField()
    time = models.DateTimeField()
    priority = models.FloatField()
    fulfilled = models.BooleanField()
    confirmtime = models.CharField(max_length=50)
    objects = Request_Manager()

class Hospital_Manager(models.Manager):
    def create_data(self, name,address,phone,total_beds,available_beds):
        details = self.create(name=name,address=address,phone=phone,total_beds=total_beds,available_beds=available_beds)
        return details

class Hospital(models.Model):
    name = models.CharField(max_length=100)
    address =  models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    total_beds = models.IntegerField()
    available_beds = models.IntegerField()
    objects = Hospital_Manager()

    def __str__(self):
        return self.name

admin.site.register(Hospital)