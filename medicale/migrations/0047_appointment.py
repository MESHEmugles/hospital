# Generated by Django 4.0.4 on 2022-05-19 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicale', '0046_delete_appointment_delete_appointment_price'),
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
                ('price', models.IntegerField(blank=True, null=True)),
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
    ]
