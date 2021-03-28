# Generated by Django 3.1.3 on 2021-03-28 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PATIENT', '0004_auto_20210328_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='heart_rate',
            field=models.DecimalField(decimal_places=2, default=200, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='spo2',
            field=models.DecimalField(decimal_places=2, default=310, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='temperature',
            field=models.DecimalField(decimal_places=2, default=100, max_digits=5),
            preserve_default=False,
        ),
    ]
