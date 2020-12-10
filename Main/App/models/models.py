from django.db import models
from Users.models import MyUsers


class Pi(models.Model):
    user = models.ForeignKey(MyUsers, related_name="user_pi", on_delete=models.CASCADE)
    key = models.CharField(max_length=100)
    decription = models.TextField(max_length=1000)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user) + ": " + self.key


class Device_Sensor(models.Model):
    pi = models.ForeignKey(Pi, related_name="pi", on_delete=models.CASCADE)
    dsid = models.IntegerField()
    decription = models.TextField(max_length=1000)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.dsid) + ": " + self.decription


class Device(models.Model):
    device = models.ForeignKey(Device_Sensor, related_name="device", on_delete=models.CASCADE)
    values = models.IntegerField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.device) + ": " + str(self.values)


class Sensor(models.Model):
    sensor = models.ForeignKey(Device_Sensor, related_name="sensor", on_delete=models.CASCADE)
    values = models.IntegerField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.sensor) + ": " + str(self.values)


class Account(models.Model):
    user = models.ForeignKey(MyUsers, related_name="user_account", on_delete=models.CASCADE)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=500)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user) + ": " + self.username