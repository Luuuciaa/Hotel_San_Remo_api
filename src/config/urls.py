"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView
#DEPENDENCIAS DE YASG
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny


# Creamos la vista del esquema para la documentación Swagger
schema_view = get_schema_view(
openapi.Info (
    title="Hotel San Remo Api",# Título que se mostrará en la documentación
    default_version='v1',# Versión de la API
    description=  'Documentación general del proyecto API REST del  Hotel San Remo '  # Descripción de la API
),
 public=True,# Indica si la documentación es pública 
 permission_classes=[AllowAny]# Permite que cualquiera acceda a ver la documentación
)


urlpatterns = [
    # Rutas (endpoints) para acceder a la documentación de la API
    #Endpoints para documentacion
      # Ruta para ver la documentación en formato Swagger
    path('swagger/',schema_view.with_ui('swagger',cache_timeout=0)),
    # Ruta para ver la documentación en formato ReDoc 
    path('redoc/',schema_view.with_ui('redoc',cache_timeout=0)),
    #Endpoint para obtener el token
    path('api/token/', TokenObtainPairView.as_view()),
    #Endpoint para refrescar el token
    path('api/token/refresh/',TokenRefreshView.as_view()),
    path('admin/', admin.site.urls),
    #Estoy asociando con un prefijo 'api/' a las rutas
    #definidas en el archivo url.py de la aplicacion api 'api'
    path('api/', include('api.urls')),  
   
]