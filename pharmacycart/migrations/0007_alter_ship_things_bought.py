# Generated by Django 4.0.4 on 2022-06-30 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacycart', '0006_ship_things_bought'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ship',
            name='things_bought',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
