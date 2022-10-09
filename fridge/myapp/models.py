from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class foodItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=128)
    # expiredate = models.DateField(null=True)
    expiredate = models.DateTimeField('expiredate')
    # expiredate = models.IntegerField(default="1")
    price = models.FloatField(default="1")