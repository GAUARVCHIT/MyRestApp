# Generated by Django 3.0.5 on 2020-06-12 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0031_auto_20200612_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peoples',
            name='mobile_no',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pointstable',
            name='kill_points',
            field=models.PositiveIntegerField(default=1, null=True),
        ),
        migrations.AlterField(
            model_name='pointstable',
            name='placement_point',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pointstable',
            name='rank',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='results',
            name='Total_points',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='results',
            name='kill_points',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='results',
            name='kills',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='results',
            name='placement_point',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='results',
            name='position',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]