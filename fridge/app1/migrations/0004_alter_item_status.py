# Generated by Django 3.2.16 on 2022-11-04 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_item_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='status',
            field=models.CharField(default='Good', max_length=100),
        ),
    ]
