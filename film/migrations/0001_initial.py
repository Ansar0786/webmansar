# Generated by Django 4.0.5 on 2022-06-09 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gateModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moviename', models.CharField(max_length=100)),
                ('poster', models.ImageField(upload_to='')),
                ('releasedate', models.DateField(auto_created='')),
                ('shortdesc', models.TextField(max_length=100)),
                ('longdesc', models.TextField(max_length=300)),
                ('publishername', models.CharField(max_length=50)),
            ],
        ),
    ]
