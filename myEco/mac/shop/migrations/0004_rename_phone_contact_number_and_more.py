# Generated by Django 4.2.2 on 2023-07-09 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact_alter_product_desc_alter_product_subcategory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='phone',
            new_name='number',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='desc',
            new_name='query',
        ),
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
