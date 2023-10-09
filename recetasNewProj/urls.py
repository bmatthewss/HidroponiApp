"""recetasNewProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from hidroponiapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.plantas, name='plantas'),
    path('consumo/', views.consumo, name='consumo'),
    path('planta/<int:planta_id>/', views.planta_detalle, name='planta_detalle'),
    path('estadisticas/', views.estadisticas, name='estadisticas'),
    path('cosechar/<int:planta_id>/', views.cosechar_planta, name='cosechar_planta'),
    path('limpiar/<int:planta_id>/', views.limpiar_planta, name='limpiar_planta'),

]
