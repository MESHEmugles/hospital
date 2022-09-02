# Generated by Django 4.0.4 on 2022-05-19 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicale', '0040_remove_appointment_price_appointment_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=50, null=True)),
                ('lastname', models.CharField(blank=True, max_length=50, null=True)),
                ('services', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=100, null=True)),
                ('apptdate', models.CharField(blank=True, max_length=200, null=True)),
                ('appt_time', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('notify', models.BooleanField(blank=True, null=True)),
                ('symptoms', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('New', 'New'), ('Pending', 'Pending'), ('Process', 'Process'), ('closed', 'Closed')], default='new', max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('closed', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Appointment',
                'verbose_name_plural': 'Appointments',
                'db_table': 'appointment',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Appointment_Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicale.appointment')),
            ],
            options={
                'verbose_name': 'Appointment_Price',
                'verbose_name_plural': 'Appointment_Prices',
                'db_table': 'appointment_price',
                'managed': True,
            },
        ),
    ]