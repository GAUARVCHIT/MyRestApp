# Generated by Django 3.0.5 on 2020-06-10 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0029_auto_20200610_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playerresult',
            name='peoples',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api_basic.Peoples'),
        ),
    ]
