from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    phone_num = models.CharField(max_length=15)
    name = models.CharField(max_length=40)
    primary_resource = models.ForeignKey("core.Resource")

    user = models.OneToOneField(User)

    def __repr__(self):
        return "UserProfile(phone_num={}, name={}, primary_resource={})".format(phone_num, name, primary_resource)


class Location (models.Model):
    name = models.CharField(max_length=250)

    def __repr__(self):
        return "Location({})".format(name)


class Resource(models.Model):
    name = models.CharField(max_length=40)

    def __repr__(self):
        return "Resource({})".format(self.name)


class Action(models.Model):
    location = models.ForeignKey("core.Location")
    active = models.BooleanField(default=False)
    requested_resources = models.ManyToManyField("core.Resource", through="core.RequestForResource", related_name="requested_at")
    pledged_resources = models.ManyToManyField("core.Resource", through="core.Pledge", related_name="pledged_to")

    def __repr__(self):
        return "Action(location={}, active={}, requested_resources={}, pledged_resources={})"


class RequestForResource(models.Model):
    """Coordinator's request for resource."""
    action = models.ForeignKey("core.Action")
    resource = models.ForeignKey("core.Resource")
    needed = models.IntegerField()
    acquired = models.IntegerField(default=0)

    def __repr__(self):
        return "RequestForResource(action={}, resource={}, needed={}, acquired={})".format(self.action,
                                                                                           self.resource,
                                                                                           self.needed,
                                                                                           self.acquired)


class Pledge(models.Model):
    """A pledge on delivering a set of resources."""
    action = models.ForeignKey("core.Action")
    resource = models.ForeignKey("core.Resource")
    pledged = models.IntegerField()

    def __repr__(self):
        return "Pledge(action={}, resource={}, pledged={})".format(self.action, self.resource, self.pledged)
