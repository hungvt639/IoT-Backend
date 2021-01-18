from django.db import models
from Users.models import MyUsers


class Chip(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(MyUsers, related_name="user_chip", on_delete=models.CASCADE)
    key = models.CharField(max_length=100, unique=True)
    decription = models.TextField(max_length=1000, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    home = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user) + ": " + self.key