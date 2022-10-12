from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class foodItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=128)
    quantity = models.IntegerField(default="1")
    expiredate = models.DateField('expiredate')
    price = models.FloatField(default="1")
