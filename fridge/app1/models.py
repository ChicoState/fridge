from datetime import date
import profile

from django.contrib.auth.models import User
from django.db import models

from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='avatar.png', upload_to='profile_pic')

    def __str__(self):
        return f'{self.user.username}'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Item(models.Model):
    STATUS_CHOICES1 = (
        ('dairy', 'dairy'),
        ('beverages', 'beverages'),
        ('frozen vegetables', 'frozen vegetables'),
        ('meat', 'meat'),
        ('fruits', 'fruits'),
    )
    STATUS = (
        ('Expired', 'Expired'),
        ('Warning', 'Warning'),
        ('Good', 'Good')
    )
       
    food_type = models.CharField(max_length=100, choices=STATUS_CHOICES1)
    food_title = models.CharField(max_length=120)
    photos = models.ImageField(upload_to='uploaded_images/')
    price = models.FloatField(blank=True, null=True, default=0)
    quantity = models.PositiveIntegerField(blank=True, null=True, default=0)
    valid_from = models.DateField(blank=True, null=True,auto_now=False, auto_now_add=False)
    valid_to = models.DateField(blank=True, null=True,auto_now=False, auto_now_add=False)
    timestamp = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    author = models.ForeignKey(Profile, default = "",on_delete=models.CASCADE)
    status = models.CharField(default='Good',max_length=100, choices=STATUS)
    delta = models.IntegerField(blank=True, null=True, default=0)
    daystill = models.IntegerField(blank=True, null=True, default=0)
    humanize_time = models.IntegerField(blank=True, null=True, default=0)
    humanize_time1 = models.IntegerField(blank=True, null=True, default=0)


    class Meta:
        verbose_name_plural = "Items"

    def __str__(self):
        return str(self.food_title)