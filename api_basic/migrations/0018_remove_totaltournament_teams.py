# Generated by Django 3.0.5 on 2020-06-07 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0017_auto_20200607_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='totaltournament',
            name='teams',
        ),
    ]
