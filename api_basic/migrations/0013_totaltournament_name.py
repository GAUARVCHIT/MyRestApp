# Generated by Django 3.0.5 on 2020-06-07 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0012_auto_20200607_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='totaltournament',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]