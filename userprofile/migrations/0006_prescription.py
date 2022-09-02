# Generated by Django 4.0.4 on 2022-05-05 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userprofile', '0005_delete_recovery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prescrip_code', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('name_of_doc', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, default='prescription.jpg', null=True, upload_to='prescription')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('disease', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=50)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
