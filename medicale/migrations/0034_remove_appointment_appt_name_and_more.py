# Generated by Django 4.0.4 on 2022-05-14 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicale', '0033_alter_appointment_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='appt_name',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='price',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='slug',
        ),
    ]
