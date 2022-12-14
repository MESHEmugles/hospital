# Generated by Django 4.0.4 on 2022-05-07 07:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medicale', '0024_subscription_plan_pricing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ship_Sub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordr_no', models.CharField(max_length=50)),
                ('itm_paid', models.BooleanField(default=False)),
                ('price', models.FloatField()),
                ('firstname', models.CharField(blank=True, max_length=200, null=True)),
                ('Pricing', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medicale.pricing')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Ship_Sub',
                'verbose_name_plural': 'Ship_Subs',
                'db_table': 'ship_sub',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Paid_Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('sub_no', models.CharField(blank=True, max_length=36, null=True)),
                ('payment_code', models.CharField(max_length=50)),
                ('paid_item', models.BooleanField(default=False)),
                ('firstname', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Paid_Subscription',
                'verbose_name_plural': 'Paid_Subscriptions',
                'db_table': 'paid_subscription',
                'managed': True,
            },
        ),
    ]
