from django.shortcuts import render
from data_banco.models import Cliente, Habitacion, Reserva

def index(request):
    cliente = Cliente.objects.first()
    habitacion = Habitacion.objects.first()

    context = {
        'cliente': cliente,
        'habitacion': habitacion
    }

    return render(request, 'front_banco/index.html', context)
