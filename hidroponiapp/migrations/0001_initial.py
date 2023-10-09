# Generated by Django 4.1.5 on 2023-04-16 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consumo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('tipo', models.CharField(choices=[('agua', 'Agua'), ('energia', 'Energía'), ('nutrientes', 'Nutrientes')], max_length=10)),
                ('cantidad', models.FloatField()),
                ('costo_por_unidad', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]