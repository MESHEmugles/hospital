# Generated by Django 4.0.4 on 2022-06-02 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicale', '0059_alter_appointment_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='price',
            field=models.CharField(default=10, max_length=2),
        ),
    ]
