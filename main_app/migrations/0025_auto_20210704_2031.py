# Generated by Django 3.1.7 on 2021-07-04 20:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0024_auto_20210703_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='credit_card',
            field=models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(regex='(?:\\d{4}-?){3}\\d{4}')]),
        ),
    ]
