# Generated by Django 3.1.3 on 2021-04-25 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PATIENT', '0005_auto_20210328_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='blood_pressure',
            field=models.IntegerField(default=110, max_length=7),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='fev1',
            field=models.IntegerField(default=4.8, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='force_vital_capacity',
            field=models.DecimalField(decimal_places=2, default=450, max_digits=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='peak_expiratory_flow',
            field=models.IntegerField(default=4, max_length=9),
            preserve_default=False,
        ),
    ]