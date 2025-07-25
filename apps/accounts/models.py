from django.db import models


class User(models.Model):
    IDUser = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(null=False, max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    inclusion = models.DateTimeField(auto_now_add=True)
