# Generated by Django 2.0.1 on 2018-10-23 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('validation', '0004_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Useful',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('useful', models.BooleanField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='validation.Company')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
