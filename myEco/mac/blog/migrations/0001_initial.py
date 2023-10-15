# Generated by Django 4.2.2 on 2023-08-02 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('postId', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('head0', models.CharField(default='', max_length=500)),
                ('head1', models.CharField(default='', max_length=500)),
                ('head2', models.CharField(default='', max_length=500)),
                ('desc', models.CharField(default='', max_length=5000)),
                ('pubDate', models.DateField()),
                ('thumbnails', models.ImageField(default='', upload_to='blog.images')),
            ],
        ),
    ]
