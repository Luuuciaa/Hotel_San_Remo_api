# 🏨 Hotel San Remo API

API REST desarrollada con Django y Django REST Framework para la gestión de un hotel. 
Permite manejar habitaciones, reservas, usuarios y administración general del Hotel San Remo.

Proyecto académico realizado por Lucía Ayelén Farrapeira como parte de la carrera *Diplomatura Universitaria En Desarrollo Web Full Stack* en UADE

---
## Autora


**Lucía Ayelen Farrapeira**  
📍 San Clemente del Tuyú, Buenos Aires
🎓 Diplomatura Universitaria En Desarrollo Web Full Stack– UADE Academy
📅 Año: 2025



## Estructura del proyecto
```
HOTEL_SAN_REMO_API/
│
├── api/   # Lógica principal (models, views, serializers, urls)
│   ├── admin.py
│   ├── middleware.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── config/     # Configuración del proyecto Django
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── habitaciones/        # Carpeta donde se guardan imágenes subidas
│
├── logs/                  # Archivos de logs personalizados
│   ├── consultas_db.log
│   ├── db_debug.log
│   ├── errores_hotel.log
│   └── hotel_san_remo_debug.log
│
├── media/                 # Archivos multimedia
│
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── manage.py
└── README.md
```

## 🚀 Funcionalidades principales

- Consultar habitaciones disponibles
- Crear, actualizar o eliminar habitaciones (solo admin)
- Crear reservas
- Consultar reservas existentes
- Autenticación de usuarios con JWT
- Docmentación de la API con Swagger
- Sistema de logs para depuración y auditoría
- Panel de administración de Django
- Preparado para deploy en Railway usando Docker

---

## 🧱 Tecnologías utilizadas

- Python 3.x
- Django
- Django REST Framework
- Simple JWT
- drf-yasg (para documentación Swagger)
- SQLite (base de datos por defecto)
- MySQL (en producción)
- Docker & Docker Compose
- Railway (deploy)

---

## 📡 Endpoints principales

🔐 Autenticación

| Método | Endpoint              | Descripción                    |
| ------ | --------------------- | ------------------------------ |
| POST   | `/api/token/`         | Obtener access + refresh token |
| POST   | `/api/token/refresh/` | Renovar token                  |


🏨 Habitaciones

| Método | Endpoint                | Descripción         |
| ------ | ----------------------- | ------------------- |
| GET    | `/api/habitacion/`      | Listar habitaciones |
| POST   | `/api/habitacion/`      | Crear habitación    |
| GET    | `/api/habitacion/<id>/` | Ver detalle         |
| PUT    | `/api/habitacion/<id>/` | Actualizar          |
| DELETE | `/api/habitacion/<id>/` | Eliminar            |


📘 Documentación interactiva
| Formato | URL         |
| ------- | ----------- |
| Swagger | `/swagger/` |


🚀 Deploy en Railway

Este proyecto incluye todo lo necesario para desplegar con Docker.

Pasos generales:

1.Subir el repo a GitHub

2.Crear servicio en Railway

3.Conectar repositorio

4.Railway detecta el Dockerfile automáticamente

5.Configurar variables de entorno

6.Deploy automático