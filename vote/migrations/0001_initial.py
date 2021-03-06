# Generated by Django 3.1.1 on 2020-09-18 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ASPL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2048)),
                ('votes', models.IntegerField(blank=True, default=0)),
                ('img_url', models.CharField(blank=True, max_length=2048)),
            ],
        ),
        migrations.CreateModel(
            name='SPL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2048)),
                ('votes', models.IntegerField(blank=True, default=0)),
                ('img_url', models.CharField(blank=True, max_length=2048)),
            ],
        ),
    ]
