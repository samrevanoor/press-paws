# Generated by Django 3.1.7 on 2021-07-04 00:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0024_auto_20210703_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='number_of_guests',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='number_of_pets',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
