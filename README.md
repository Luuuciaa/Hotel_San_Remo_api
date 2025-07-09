# 🏨 Hotel San Remo API

API REST desarrollada con Django y Django REST Framework para la gestión de un hotel. 
Permite manejar habitaciones, reservas, usuarios y administración general del Hotel San Remo.

Proyecto académico realizado por Lucía Ayelén Farrapeira como parte de la carrera *Diplomatura Universitaria En Desarrollo Web Full Stack* en UADE

---
## Autora
```
**Lucía Ayelen Farrapeira**  
📍 San Clemente del Tuyú, Buenos Aires
🎓 Diplomatura Universitaria En Desarrollo Web Full Stack– UADE Academy
📅 Año: 2025
```


## Estructura del proyecto
```
HOTEL_SAN_REMO_API/
├── api/ # Lógica de la app (views, models, serializers, urls)
├── config/ # Configuración del proyecto Django
├── manage.py # Comando principal
├── requirements.txt # Lista de dependencias
├── db.sqlite3 # Base de datos por defecto
└── README.md # Este archivo
```

## 🚀 Funcionalidades principales

- Consultar habitaciones disponibles
- Crear, actualizar o eliminar habitaciones (admin)
- Crear reservas
- Consultar reservas existentes
- Autenticación de usuarios con JWT (JSON Web Tokens)
- Documentación interactiva con Swagger

---

## 🧱 Tecnologías utilizadas

- Python 3.x
- Django
- Django REST Framework
- Simple JWT
- drf-yasg (para documentación Swagger)
- SQLite (base de datos por defecto)

---

## 📡 Endpoints principales

| Método | Endpoint            | Descripción                         |
|--------|---------------------|-------------------------------------|
| GET    | /api/habitaciones/  | Listar habitaciones                 |
| POST   | /api/reservas/      | Crear reserva                       |
| GET    | /api/reservas/      | Consultar reservas                  |
| POST   | /api/token/         | Obtener tokens de acceso JWT        |
| GET    | /swagger/           | Ver documentación Swagger           |

---