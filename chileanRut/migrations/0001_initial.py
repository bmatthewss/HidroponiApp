# Generated by Django 4.1.5 on 2023-01-25 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=255)),
                ('rut', models.CharField(max_length=100)),
                ('sexo', models.CharField(blank=True, max_length=100)),
                ('direccion', models.CharField(blank=True, max_length=255)),
                ('ciudad', models.CharField(blank=True, max_length=100)),
                ('estado', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
