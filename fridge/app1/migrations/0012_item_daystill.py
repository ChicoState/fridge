# Generated by Django 3.0.9 on 2022-11-28 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_auto_20221125_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='daystill',
            field=models.IntegerField(default=0),
        ),
    ]
