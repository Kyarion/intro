# Generated by Django 4.2.6 on 2023-11-01 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mision', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='misiones',
            new_name='Task',
        ),
    ]