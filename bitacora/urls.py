from django.urls import path #reverse_lazy
# from django.views.generic import RedirectView
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Ruta para la página de inicio
    path('login/', LoginView.as_view(), name='login'),  # Ruta para inicio de sesión
    path('logout/', LogoutView.as_view(), name='logout'),  # Ruta para cierre de sesión
    path('agregar/', views.agregar_actividad, name='agregar_actividad'),
    path('registro/', views.registro, name='registro'),  # Ruta para registro
    path('imprimir_bitacora/', views.imprimir_bitacora, name='imprimir_actividades'),
    # Agrega más rutas según las necesidades de tu aplicación
]
