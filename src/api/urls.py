from django.urls import path
from . import views


urlpatterns = [
    path('hola_mundo/', views.inicio),  
    path('api_info/', views.api_info),
    path('habitacion/', views.HabitacionAPIView.as_view()),
    path('habitacion/<int:id_habitacion>', views.HabitacionDetalleAPIView.as_view()),
    path('reserva/<int:id_reserva>/', views.ReservaAPIView.as_view()), 
]