# Generated by Django 4.0.4 on 2022-05-04 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicale', '0007_alter_appointment_phone_number'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Appointment',
        ),
    ]
