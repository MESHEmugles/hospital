# Generated by Django 4.0.4 on 2022-06-30 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicale', '0066_alter_ship_sub_things_bought'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='price',
            field=models.FloatField(default=10, max_length=2),
        ),
    ]
