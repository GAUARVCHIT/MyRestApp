# Generated by Django 3.0.5 on 2020-06-06 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0003_auto_20200605_1956'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seasons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]