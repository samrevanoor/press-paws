# Generated by Django 3.1.7 on 2021-06-28 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_merge_20210627_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='total_owed',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
    ]
