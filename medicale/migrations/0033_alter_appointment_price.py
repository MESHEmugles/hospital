# Generated by Django 4.0.4 on 2022-05-14 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicale', '0032_alter_appointment_appt_name_alter_appointment_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='price',
            field=models.IntegerField(blank=True, default=10, null=True),
        ),
    ]