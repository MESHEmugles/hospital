# Generated by Django 4.0.4 on 2022-04-25 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_alter_profile_fullname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='fullname',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
