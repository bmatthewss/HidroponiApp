# Generated by Django 4.1.5 on 2023-04-16 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hidroponiapp', '0002_alter_consumo_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('lechuga', 'Lechuga'), ('espinaca', 'Espinaca'), ('tomate', 'Tomate')], max_length=20)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField(blank=True, null=True)),
                ('estado', models.CharField(choices=[('viva', 'Viva'), ('muerta', 'Muerta'), ('consumida', 'Consumida')], max_length=10)),
            ],
        ),
    ]
