from django.db import models
from django.utils import timezone

# Create your models here.
class reservation(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=300)
    phone = models.IntegerField(max_length=10)
    noofguests = models.IntegerField(max_length=3)
    rdate = models.DateField(default=timezone.now())
    rtime = models.TimeField(default= timezone.now())
    reservationtype = models.CharField(max_length=200)
    mention = models.TextField()

class buffet(models.Model):
    bdate = models.DateField(default= timezone.now())
    btime = models.TimeField(default= timezone.now())
    partysize = models.IntegerField(max_length=3)
    bfirst_name = models.CharField(max_length=100)
    blast_name = models.CharField(max_length=100)
    bemail = models.EmailField(max_length=300)
    bphone = models.IntegerField(max_length=10)
    blocation = models.CharField(max_length=200)
    address = models.TextField()

class items(models.Model):
    img = models.ImageField(upload_to="pics")
    description = models.CharField(max_length=500)
    price = models.IntegerField(max_length=3)
    itemname = models.CharField(max_length=50)
    keep = models.BooleanField(default = "False")

class menu(models.Model):
    item = models.CharField(max_length=50)
    price = models.IntegerField()
    itemof = models.CharField(max_length=20)
    keep = models.BooleanField(default="False")

