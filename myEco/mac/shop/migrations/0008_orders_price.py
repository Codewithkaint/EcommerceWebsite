# Generated by Django 4.2.2 on 2023-08-12 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_orders_json'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='price',
            field=models.IntegerField(default=0, max_length=100),
        ),
    ]
