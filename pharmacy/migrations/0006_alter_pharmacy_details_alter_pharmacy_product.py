# Generated by Django 4.0.4 on 2022-05-01 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0005_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pharmacy',
            name='details',
            field=models.TextField(default='o'),
        ),
        migrations.AlterField(
            model_name='pharmacy',
            name='product',
            field=models.CharField(default='o', max_length=150, unique=True),
        ),
    ]
