# Generated by Django 3.0.9 on 2022-12-02 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0017_auto_20221201_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='wday',
        ),
    ]
