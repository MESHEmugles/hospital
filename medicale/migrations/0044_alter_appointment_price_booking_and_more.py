# Generated by Django 4.0.4 on 2022-05-19 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicale', '0043_appointment_price_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment_price',
            name='booking',
            field=models.CharField(blank=True, default='appoitment', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='appointment_price',
            name='price',
            field=models.IntegerField(blank=True, default=10, null=True),
        ),
    ]
