from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    gender= models.CharField(max_length=30)
    address= models.CharField(max_length=30)


class cc_fraud_detection_type(models.Model):

    trans_date= models.CharField(max_length=300)
    cc_num= models.CharField(max_length=300)
    category= models.CharField(max_length=300)
    AMT_TRANS= models.CharField(max_length=300)
    first= models.CharField(max_length=300)
    last= models.CharField(max_length=300)
    gender= models.CharField(max_length=300)
    street= models.CharField(max_length=300)
    city= models.CharField(max_length=300)
    state= models.CharField(max_length=300)
    zip= models.CharField(max_length=300)
    User_Lat= models.CharField(max_length=300)
    User_Long= models.CharField(max_length=300)
    city_pop= models.CharField(max_length=300)
    Job= models.CharField(max_length=300)
    Dob= models.CharField(max_length=300)
    trans_num= models.CharField(max_length=300)
    merch_lat= models.CharField(max_length=300)
    merch_long= models.CharField(max_length=300)
    Prediction= models.CharField(max_length=300)


class detection_accuracy(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

class detection_ratio(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)



