# Generated by Django 4.2.2 on 2023-08-12 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_alter_orders_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='price',
        ),
        migrations.AddField(
            model_name='orders',
            name='prices',
            field=models.CharField(default='', max_length=100),
        ),
    ]
