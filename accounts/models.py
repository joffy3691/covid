from django.db import models
from django.contrib.auth.models import User


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