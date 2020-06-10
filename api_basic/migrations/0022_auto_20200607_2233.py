# Generated by Django 3.0.5 on 2020-06-07 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0021_auto_20200607_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='days',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='matches',
            name='teams',
            field=models.ManyToManyField(to='api_basic.Teams'),
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(blank=True, null=True)),
                ('kills', models.IntegerField(blank=True, null=True)),
                ('teams', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='api_basic.Teams')),
            ],
        ),
        migrations.AddField(
            model_name='matches',
            name='results',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='api_basic.Results'),
        ),
    ]