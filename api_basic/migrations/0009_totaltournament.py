# Generated by Django 3.0.5 on 2020-06-06 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0008_seasons_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='TotalTournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api_basic.Seasons')),
            ],
        ),
    ]
