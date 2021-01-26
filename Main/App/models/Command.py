from django.db import models
from Users.models import MyUsers


class Command(models.Model):
    user = models.ForeignKey(MyUsers, on_delete=models.CASCADE)
    key = models.CharField(max_length=100)
    pin_id = models.IntegerField()
    command = models.IntegerField()
    create_at = models.DateTimeField()

    def __str__(self):
        return "{}: {} : {}: {}".format(self.user, self.key, self.pin_id, self.command)


class CommandRespose(models.Model):
    command_id = models.ForeignKey(Command, related_name="response", on_delete=models.CASCADE)
    data = models.IntegerField()
    create_at = models.DateTimeField()

    def __str__(self):
        return "{}: {}".format(self.command_id, self.data)