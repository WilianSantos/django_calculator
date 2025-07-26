from django.db import models
from django.contrib.auth.hashers import make_password, check_password


class User(models.Model):
    user_id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(null=False, blank=False, max_length=100)
    email = models.EmailField(unique=True, null=False, blank=False)
    password = models.CharField(max_length=128, null=False, blank=False)
    inclusion = models.DateTimeField(auto_now_add=True)

    def set_password(self, flat_password):
        self.password = make_password(flat_password)

    def check_password(self, flat_password):
        return check_password(flat_password, self.password)
