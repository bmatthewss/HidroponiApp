from datetime import date

from django.shortcuts import render, get_object_or_404, redirect
from .models import Consumo
from .forms import ConsumoForm
from django.contrib import messages
from .models import Planta
from .forms import PlantaForm
from collections import Counter, defaultdict


def consumo(request):
    if request.method == 'POST':
        form = ConsumoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro de consumo guardado correctamente.')
        else:
            messages.error(request, 'Por favor, completa todos los campos requeridos.')

    else:
        form = ConsumoForm()

    consumos = Consumo.objects.all()
    return render(request, 'hidroponiapp/consumo.html', {'form': form, 'consumos': consumos})

def plantas(request):
    plantas = Planta.objects.all().order_by('-fecha_inicio')
    form = PlantaForm()

    if request.method == 'POST':
        form = PlantaForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'plantas': plantas,
        'form': form,
    }
    return render(request, 'hidroponiapp/plantas.html', context)


def cosechar_planta(request, planta_id):
    planta = Planta.objects.get(pk=planta_id)
    planta.estado = Planta.COSECHADA
    planta.fecha_fin = date.today()
    planta.save()
    return redirect(
        'plantas')  # Reemplaza 'plantas' con el nombre de la URL de la vista de la lista de plantas, si es diferente

def limpiar_planta(request, planta_id):
    planta = Planta.objects.get(pk=planta_id)
    planta.estado = Planta.MUERTA
    planta.fecha_fin = date.today()
    planta.save()
    return redirect(
        'plantas')  # Reemplaza 'plantas' con el nombre de la URL de la vista de la lista de plantas, si es diferente



def planta_detalle(request, planta_id):
    planta = get_object_or_404(Planta, id=planta_id)
    context = {
        'planta': planta,
    }
    return render(request, 'hidroponiapp/planta_detalle.html', context)


def estadisticas(request):

    consumos = Consumo.objects.all()
    consumos_mensuales = defaultdict(lambda: defaultdict(float))

    for consumo in consumos:
        mes_anio = date(consumo.fecha.year, consumo.fecha.month, 1)
        consumos_mensuales[mes_anio][consumo.tipo] += consumo.cantidad

    meses = list(consumos_mensuales.keys())
    consumos_agua = [consumos_mensuales[mes]['Agua'] for mes in meses]
    consumos_energia = [consumos_mensuales[mes]['Energía'] for mes in meses]
    consumos_nutrientes = [consumos_mensuales[mes]['Nutrientes'] for mes in meses]

    meses_str = [mes.strftime('%b %Y') for mes in meses]

    plantas = Planta.objects.all()
    vivas = plantas.filter(estado='Viva').count()
    muertas = plantas.filter(estado='Muerta').count()
    cosechadas = plantas.filter(estado='Cosechada').count()
    plantas_vivas = Planta.objects.filter(estado=Planta.VIVA)
    plantas_muertas = Planta.objects.filter(estado=Planta.MUERTA)
    tipos_vivos = Counter(planta.tipo for planta in plantas_vivas)
    tipos_muertos = Counter(planta.tipo for planta in plantas_muertas)
    tipos_labels = [nombre for nombre, cantidad in tipos_vivos.items()]
    tipos_vivas = [cantidad for nombre, cantidad in tipos_vivos.items()]
    tipos_muertas = [cantidad for nombre, cantidad in tipos_muertos.items()]


    mes_actual = date.today().replace(day=1)
    costos_mensuales = defaultdict(lambda: defaultdict(float))

    for consumo in consumos:
        mes_anio = date(consumo.fecha.year, consumo.fecha.month, 1)
        consumos_mensuales[mes_anio][consumo.tipo] += consumo.cantidad

        # Calcula el costo total sólo si el consumo es del mes actual
        print(mes_anio)
        print(mes_actual)
        print(consumo.cantidad)
        if mes_anio == mes_actual:
            costos_mensuales[mes_anio][f"{consumo.tipo}_costo"] += consumo.costo_total()

    costos_agua_actual = [costos_mensuales[mes_actual]['Agua_costo']]
    costos_energia_actual = [costos_mensuales[mes_actual]['Energía_costo']]
    costos_nutrientes_actual = [costos_mensuales[mes_actual]['Nutrientes_costo']]

    print(costos_agua_actual)
    print(consumos_agua)

    context = {
        'tipos_labels': tipos_labels,
        'tipos_vivas': tipos_vivas,
        'tipos_muertas': tipos_muertas,
        'vivas': vivas,
        'muertas': muertas,
        'cosechadas': cosechadas,
        'meses': meses_str,
        'consumos_agua': consumos_agua,
        'consumos_energia': consumos_energia,
        'consumos_nutrientes': consumos_nutrientes,
        'costos_agua': costos_agua_actual,
        'costos_energia': costos_energia_actual,
        'costos_nutrientes': costos_nutrientes_actual,
    }
    return render(request, 'hidroponiapp/estadisticas.html', context)