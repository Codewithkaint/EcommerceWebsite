# Generated by Django 4.2.2 on 2023-07-24 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_tracker'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='json',
            field=models.CharField(default='', max_length=3000),
        ),
    ]