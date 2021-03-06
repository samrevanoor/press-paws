# Generated by Django 3.1.7 on 2021-07-01 01:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_auto_20210630_0332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date_to',
            field=models.DateField(default=datetime.date(2021, 7, 2)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='number_of_nights',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='total_owed',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
