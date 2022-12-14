# Generated by Django 4.0.4 on 2022-05-06 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacycart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordr_no', models.CharField(max_length=50)),
                ('itm_paid', models.BooleanField(default=False)),
                ('total', models.FloatField()),
                ('fullname', models.CharField(blank=True, max_length=150, null=True)),
                ('date_of_birth', models.CharField(blank=True, max_length=250, null=True)),
                ('company_name', models.CharField(blank=True, max_length=250, null=True)),
                ('phone_number', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('zip', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('New', 'New'), ('Pending', 'Pending'), ('Processing', 'Processing'), ('Shipping', 'Shipping'), ('Delivered', 'Delivered')], max_length=50)),
                ('admin_remark', models.CharField(max_length=250)),
                ('drugscart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacycart.drugscart')),
            ],
            options={
                'verbose_name': 'Checkout',
                'verbose_name_plural': 'Checkouts',
                'db_table': 'checkout',
                'managed': True,
            },
        ),
    ]
