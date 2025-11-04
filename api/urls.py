from django.urls import path
from . import views

from rest_framework.routers import DefaultRouter
router = DefaultRouter ()
#Genera las rutas de forma dinamica en base al ViewSet
router.register (r'habitaciones', views.HabitacionViewSet , basename = 'habitaciones')

urlpatterns = [
    path('hola_mundo/', views.inicio),  
    path('api_info/', views.api_info),
    path('habitacion/', views.HabitacionAPIView.as_view()),
    path('habitacion/<int:id_habitacion>/', views.HabitacionDetalleAPIView.as_view()),
    path('reserva/<int:id_reserva>/', views.ReservaAPIView.as_view()), 
]

#Sumamos al listado de rutas generadas automaticamente
urlpatterns += router.urls