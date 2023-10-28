from django.db import models
from user import models as UserModel
from django.utils import timezone


# Create your models here.


class Competition(models.Model):
    alphabet = models.CharField(max_length=1)
    create_date = models.DateTimeField(default=timezone.localtime, blank=True)
    complete = models.BooleanField(default=False)


class Participation(models.Model):
    player = models.ForeignKey(UserModel.User, on_delete=models.DO_NOTHING, null=True)
    competition = models.ForeignKey(Competition, on_delete=models.DO_NOTHING, null=True)
    date = models.DateTimeField(default=timezone.localtime, blank=True)


class Paper(models.Model):
    class Type:
        FNAME = "firs_name"
        LNAME = "last_name"
        CITY = "city"
        COUNTRY = "country"
        ANIMAL = "animal"
        COLOR = "color"

    TYPE_CHOICES = [
        (Type.FNAME, Type.FNAME),
        (Type.LNAME, Type.LNAME),
        (Type.CITY, Type.CITY),
        (Type.COUNTRY, Type.COUNTRY),
        (Type.ANIMAL, Type.ANIMAL),
        (Type.COLOR, Type.COLOR),
    ]
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, null=True)
    player = models.ForeignKey(UserModel.User, on_delete=models.DO_NOTHING)
    competition = models.ForeignKey(Competition, on_delete=models.DO_NOTHING)
    value = models.CharField(max_length=50, blank=True, null=True)
    score = models.IntegerField(null=True)
    date = models.DateTimeField(default=timezone.localtime, blank=True)
