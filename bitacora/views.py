from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .models import Actividad
from .forms import ActividadForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
#from datetime import datetime
import datetime
from django.utils import timezone
from django.contrib.auth.decorators import login_required  # Importa el decorador login_required


# Create your views here.

def index(request):
    user = request.user
    # Obten la fecha actual
    fecha_actual = datetime.date.today()
    # Filtra las actividades del usuario para el mes actual
    actividades = Actividad.objects.filter(empleado=user, fecha__month=fecha_actual.month)

    # Verifica si no hay actividades para el mes actual
    if not actividades.exists():
        # Si no hay actividades, crea una nueva actividad para el día actual
        nueva_actividad = Actividad(empleado=user, fecha=fecha_actual)
        nueva_actividad.save()
        # Actualiza la lista de actividades para incluir la nueva actividad
        actividades = Actividad.objects.filter(empleado=user, fecha__month=fecha_actual.month)

    return render(request, 'bitacora/index.html', {'actividades': actividades})

@login_required(login_url='login')
def agregar_actividad(request):
    if request.method == 'POST':
        form = ActividadForm(request.POST)
        if form.is_valid():
            actividad = form.save(commit=False)
            actividad.empleado = request.user  # Asocia la actividad al usuario actual
            actividad.save()
            return redirect('index')
    else:
        form = ActividadForm()
    return render(request, 'bitacora/agregar_actividad.html', {'form': form})

# Vista para registrar un nuevo usuario
def registro(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        messages.success(request, 'Registro exitoso.')
        return redirect('index')
    return render(request, 'registration/registro.html')

# Vista para iniciar sesión
def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Inicio de sesión exitoso.')
            return redirect('index')
        else:
            messages.error(request, 'Inicio de sesión fallido. Por favor, verifica tus credenciales.')
    return render(request, 'registration/login.html')

# Vista para cerrar sesión
def cerrar_sesion(request):
    logout(request)
    messages.success(request, 'Cierre de sesión exitoso.')
    return redirect('index')

#@login_required
#def imprimir_bitacora(request):
    # Obtén el mes y año actual
 #   fecha_actual = timezone.now()
 #   mes_actual = fecha_actual.month
 #   año_actual = fecha_actual.year
    
    # Filtra las actividades para el mes y año especificados
 #   actividades = Actividad.objects.filter(fecha__month=mes_actual, fecha__year=año_actual)
    
    # Organiza las actividades por empleado y luego por fecha
 #   actividades = actividades.order_by('empleado__username', 'fecha')

 #   # Obtén el nombre del mes en formato legible
  #  nombre_mes = fecha_actual.strftime('%B')

    
 #   context = {
 #       'actividades': actividades,
 #       'mes_actual': nombre_mes,
 #       'año_actual': año_actual,
 #   }
    
 #   return render(request, 'impresion/imprimir.html', context)
 
# En tu vista Django
from itertools import groupby

def imprimir_bitacora(request):
    # Obtén el mes y año actual
    fecha_actual = timezone.now()
    mes_actual = fecha_actual.month
    año_actual = fecha_actual.year
    
    # Filtra las actividades para el mes y año especificados
    actividades = Actividad.objects.filter(fecha__month=mes_actual, fecha__year=año_actual)
    
    # Organiza las actividades por empleado y luego por fecha
    actividades = actividades.order_by('empleado__username', 'fecha')

    # Obtén el nombre del mes en formato legible
    nombre_mes = fecha_actual.strftime('%B')

    # Organiza las actividades en una lista de tuplas (empleado, actividades)
    actividades_por_empleado = []
    for key, group in groupby(actividades, key=lambda x: x.empleado):
        actividades_por_empleado.append((key, list(group)))

    context = {
        'actividades_por_empleado': actividades_por_empleado,
        'mes_actual': nombre_mes,
        'año_actual': año_actual,
    }
    
    return render(request, 'impresion/imprimir.html', context)
    

