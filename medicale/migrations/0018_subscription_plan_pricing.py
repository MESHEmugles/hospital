# Generated by Django 4.0.4 on 2022-05-07 06:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medicale', '0017_delete_pricing_delete_subscription_plan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription_plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField(unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Subscription_plan',
                'verbose_name_plural': 'Subscription_plans',
                'db_table': 'subscription_plan',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscription_price', models.IntegerField()),
                ('individual', models.BooleanField()),
                ('family', models.BooleanField()),
                ('premium', models.BooleanField()),
                ('hmo', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('subscription_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicale.subscription_plan')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Pricing',
                'verbose_name_plural': 'Pricings',
                'db_table': 'pricing',
                'managed': True,
            },
        ),
    ]
