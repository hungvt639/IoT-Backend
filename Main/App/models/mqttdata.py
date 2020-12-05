from django.db import models
from Users.models import MyUsers


class Data(models.Model):
    name = models.CharField(max_length=100)
    # user = models.ForeignKey(MyUsers, on_delete=models.CASCADE, related_name='user')
    status = models.BooleanField(default=False)
    number = models.IntegerField()

    def __str__(self):
        return self.name