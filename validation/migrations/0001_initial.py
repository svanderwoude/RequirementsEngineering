# Generated by Django 2.0.1 on 2018-10-14 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnchoringResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('version', models.FloatField()),
                ('result', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
