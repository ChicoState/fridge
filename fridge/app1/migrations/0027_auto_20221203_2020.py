# Generated by Django 3.0.9 on 2022-12-04 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0026_auto_20221203_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='valid_from',
            field=models.DateField(default=''),
        ),
        migrations.AlterField(
            model_name='item',
            name='valid_to',
            field=models.DateField(default=''),
        ),
    ]