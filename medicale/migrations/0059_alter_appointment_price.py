# Generated by Django 4.0.4 on 2022-06-02 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicale', '0058_alter_appointment_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='price',
            field=models.CharField(default=10, editable=False, max_length=2),
        ),
    ]
