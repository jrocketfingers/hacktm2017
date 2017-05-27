from django.db import models


# Create your models here.
class Location (models.Model):
    name = models.CharField(max_length=250)


class Equipment(models.Model):
    name = models.CharField(max_length=40)


class Action(models.Model):
    location = models.ForeignKey(Location)
    primary_resource = models.ForeignKey(Equipment)
    active = models.BooleanField(default=False)
    equipment = models.ManyToManyField(Equipment, through=ActionEqu)


class Person(models.Model):
    phone_num = models.CharField(max_length=15)
    name = models.CharField(max_length=40)


class ActionEqu(models.Model):
    action = models.ForeignKey(Action)
    equipment = models.ForeignKey(Equipment)
    needed = models.IntegerField()
    acquired = models.IntegerField(default=0)