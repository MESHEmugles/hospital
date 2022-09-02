# Generated by Django 4.0.4 on 2022-05-10 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacycart', '0003_ship_paidorder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drugscart',
            name='pharmacy',
        ),
        migrations.RemoveField(
            model_name='drugscart',
            name='user',
        ),
        migrations.RemoveField(
            model_name='paidorder',
            name='user',
        ),
        migrations.RemoveField(
            model_name='ship',
            name='pharmacy',
        ),
        migrations.RemoveField(
            model_name='ship',
            name='user',
        ),
        migrations.DeleteModel(
            name='Checkout',
        ),
        migrations.DeleteModel(
            name='Drugscart',
        ),
        migrations.DeleteModel(
            name='Paidorder',
        ),
        migrations.DeleteModel(
            name='Ship',
        ),
    ]
