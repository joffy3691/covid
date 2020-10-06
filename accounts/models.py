from django.db import models
from django.contrib.auth.models import User
import datetime

class Activation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)

class User_AttributesManager(models.Manager):
    def create_data(self, user,details_filled,age,gender,bmi,fever,cough,spo2,breathing,pregnant,smoker,alcoholic,
                    diabetic,cancer,ckd,copd,autoimmune,immunocompromised,heart,asthma,blood,liver):
        details = self.create(user=user,details_filled=details_filled,age=age,gender=gender,bmi=bmi,fever=fever,cough=cough,spo2=spo2,breathing=breathing,pregnant=pregnant,
                              smoker=smoker,alcoholic=alcoholic,diabetic=diabetic,cancer=cancer,ckd=ckd,copd=copd
                              ,autoimmune=autoimmune,immunocompromised=immunocompromised,heart=heart,
                              asthma=asthma,blood=blood,liver=liver)
        return details

class User_Attributes(models.Model):
    user = models.IntegerField()
    details_filled = models.BooleanField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    bmi = models.FloatField()
    fever = models.FloatField()
    cough = models.BooleanField()
    spo2 = models.FloatField()
    breathing = models.BooleanField()
    pregnant = models.BooleanField()
    smoker = models.BooleanField()
    alcoholic = models.BooleanField()
    diabetic = models.BooleanField()
    cancer = models.BooleanField()
    ckd = models.BooleanField()
    copd = models.BooleanField()
    autoimmune = models.BooleanField()
    immunocompromised = models.BooleanField()
    heart = models.BooleanField()
    asthma = models.BooleanField()
    blood = models.BooleanField()
    liver = models.BooleanField()
    objects = User_AttributesManager()

class Request_Manager(models.Manager):
    def create_data(self, user,hospital):
        details = self.create(user=user,hospital=hospital,time=datetime.datetime.now())
        return details

class Request(models.Model):
    user = models.IntegerField()
    hospital =  models.IntegerField()
    time = models.DateTimeField()
    objects = Request_Manager()

class Hospital_Manager(models.Manager):
    def create_data(self, name,address,phone):
        details = self.create(name=name,address=address,phone=phone)
        return details

class Hospital(models.Model):
    name = models.CharField(max_length=100)
    address =  models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    objects = Hospital_Manager()