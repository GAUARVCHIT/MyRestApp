# Generated by Django 3.0.5 on 2020-06-05 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0002_customers_order_product_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tag',
            field=models.ManyToManyField(related_name='products_tag', to='api_basic.Tag'),
        ),
    ]
