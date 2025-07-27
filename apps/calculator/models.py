from django.db import models

from apps.accounts.models import User


class Operation(models.Model):
    operation_id = models.IntegerField(primary_key=True, auto_created=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    parameters = models.CharField(null=False, blank=False, max_length=30)
    result = models.CharField(null=False, blank=False, max_length=30)
    inclusion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user_id)
