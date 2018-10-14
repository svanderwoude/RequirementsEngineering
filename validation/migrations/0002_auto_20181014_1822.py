# Generated by Django 2.0.1 on 2018-10-14 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorityResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('version', models.PositiveIntegerField(verbose_name='Getoond bedrijfsformaat')),
                ('result', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='anchoringresult',
            name='version',
            field=models.FloatField(verbose_name='Getoond gemiddelde'),
        ),
    ]
