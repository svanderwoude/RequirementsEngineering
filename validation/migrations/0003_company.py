# Generated by Django 2.0.1 on 2018-10-23 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validation', '0002_auto_20181014_1822'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=64)),
                ('clicks', models.PositiveIntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
