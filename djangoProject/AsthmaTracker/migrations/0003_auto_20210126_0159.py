# Generated by Django 3.1.3 on 2021-01-25 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AsthmaTracker', '0002_doctoruser'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DoctorUser',
            new_name='User',
        ),
    ]
