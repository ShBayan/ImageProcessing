# Generated by Django 2.0.7 on 2018-09-16 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImagesInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('imageName', models.CharField(blank=True, default='', max_length=500)),
                ('imageURL', models.CharField(blank=True, default='', max_length=2000)),
                ('vendorName', models.CharField(blank=True, default='', max_length=200)),
                ('collectionName', models.CharField(blank=True, default='', max_length=500)),
                ('designName', models.CharField(blank=True, default='', max_length=500)),
                ('isDone', models.BooleanField(default=False)),
            ],
        ),
    ]
