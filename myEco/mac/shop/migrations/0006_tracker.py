# Generated by Django 4.2.2 on 2023-07-20 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('updated_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default='')),
                ('new_desc', models.CharField(max_length=300)),
                ('time', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
