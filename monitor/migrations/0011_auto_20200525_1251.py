# Generated by Django 3.0.2 on 2020-05-25 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0010_auto_20200321_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipement',
            name='aeroport',
            field=models.CharField(choices=[('MJ', 'majdi'), ('YS', 'yasin')], default='MJ', max_length=30),
        ),
        migrations.AlterField(
            model_name='technicien',
            name='nom',
            field=models.CharField(max_length=40),
        ),
    ]
