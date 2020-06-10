# Generated by Django 3.0.5 on 2020-06-08 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0024_auto_20200608_1154'),
    ]

    operations = [
        migrations.CreateModel(
            name='PointsTableType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PointsTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(null=True)),
                ('placement_point', models.IntegerField(null=True)),
                ('kill_points', models.IntegerField(default=1, null=True)),
                ('pointsTableType', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api_basic.PointsTableType')),
            ],
        ),
    ]