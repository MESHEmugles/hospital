# Generated by Django 4.0.4 on 2022-05-14 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicale', '0031_appointment_appt_name_appointment_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appt_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='slug',
            field=models.SlugField(),
        ),
    ]
