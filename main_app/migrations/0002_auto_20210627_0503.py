# Generated by Django 3.1.7 on 2021-06-27 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='credit_card',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='room',
            name='capacity',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('D', 'Dog'), ('C', 'Cat')], default='D', max_length=1)),
                ('breed', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.profile')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
