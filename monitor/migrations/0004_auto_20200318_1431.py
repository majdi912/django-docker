# Generated by Django 3.0.2 on 2020-03-18 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0003_auto_20200318_1353'),
    ]

    operations = [
        migrations.RenameField(
            model_name='technicien',
            old_name='nom',
            new_name='name',
        ),
    ]
