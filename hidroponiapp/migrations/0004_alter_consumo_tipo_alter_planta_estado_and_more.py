# Generated by Django 4.1.5 on 2023-04-28 23:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hidroponiapp', '0003_planta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumo',
            name='tipo',
            field=models.CharField(choices=[('Agua', 'Agua'), ('Energía', 'Energía'), ('Nutrientes', 'Nutrientes')], max_length=10),
        ),
        migrations.AlterField(
            model_name='planta',
            name='estado',
            field=models.CharField(choices=[('Viva', 'Viva'), ('Muerta', 'Muerta'), ('Cosechada', 'Cosechada')], default='Viva', max_length=10),
        ),
        migrations.AlterField(
            model_name='planta',
            name='fecha_inicio',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='planta',
            name='tipo',
            field=models.CharField(choices=[('Lechuga', 'Lechuga'), ('Espinaca', 'Espinaca'), ('Tomate', 'Tomate')], max_length=20),
        ),
    ]
