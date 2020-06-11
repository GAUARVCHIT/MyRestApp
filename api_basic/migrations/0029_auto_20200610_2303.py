# Generated by Django 3.0.5 on 2020-06-10 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0028_auto_20200610_2220'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='community',
            options={'verbose_name_plural': 'Community'},
        ),
        migrations.AlterModelOptions(
            name='peoples',
            options={'verbose_name_plural': 'Peoples'},
        ),
        migrations.CreateModel(
            name='PlayerResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kills', models.PositiveIntegerField(default=0, null=True)),
                ('damageDealt', models.PositiveIntegerField(default=0, null=True)),
                ('knockout', models.PositiveIntegerField(default=0, null=True)),
                ('matches', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api_basic.Matches')),
                ('peoples', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='api_basic.Peoples')),
                ('teams', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api_basic.Teams')),
            ],
            options={
                'verbose_name_plural': 'PlayerResult',
            },
        ),
    ]
