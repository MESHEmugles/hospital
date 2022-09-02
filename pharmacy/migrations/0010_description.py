# Generated by Django 4.0.4 on 2022-05-02 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0009_delete_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overview', models.TextField()),
                ('effect', models.CharField(blank=True, max_length=300, null=True)),
                ('ingredient', models.CharField(blank=True, max_length=300, null=True)),
                ('how_to_use', models.TextField()),
                ('advice', models.TextField()),
                ('display', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('drug_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.drug_type')),
                ('pharmacy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.pharmacy')),
            ],
            options={
                'verbose_name': 'Description',
                'verbose_name_plural': 'Descriptions',
                'db_table': 'description',
                'managed': True,
            },
        ),
    ]