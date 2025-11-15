
from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse
from rest_framework.views import APIView
from .models import Habitacion , Reserva
from .serializers import HabitacionSerializers , ReservaReadSerializer
from rest_framework.response import Response 
from rest_framework import status
#Permisos
from rest_framework.permissions import IsAuthenticated ,IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication



#Logging
import logging
#Instancia del logger de la app
logger = logging.getLogger('hotel_san_remo_api')# Logger generales


# Create your views here.
def inicio (request):
    mensaje = "<h1> HOTEL SAN REMO </h1>" 
    return HttpResponse(mensaje)
 
def api_info(request):

    """
    Información general de la API de San Remo 

    """

    response = {
        "message ": "Bienvenido a la API de San Remo",
        "version" : "1.0"
    }
    return JsonResponse (response)
    

#def api_habitaciones(request) :
   # habitaciones = {
      #  'titulo': 'Doble Standard',
       # 'precio' : 35000,
     #   'cantidad de personas' : 2,
     #   'descripcion': 'Habitación con cama matrimonial, wifi, TV, baño privado, ropa de cama y baño, y ventilador de techo',
      #  }
    #return JsonResponse (habitaciones)
    

# ---------------- HABITACIONES ---------------- #

#Cualquier petición a HabitacionAPIView o HabitacionDetalleAPIView requiere un token JWT válido.

class HabitacionAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication] # Va a usar autenticación JWT para validar al usuario antes de permitir el acceso.
    #PETICIÓN GET → lista todas las habitaciones
    #Obtenemos todas las habitaciones
    def get(self, request):
        # Voy a buscar las habitaciones en mi base de datos 
        habitacion = Habitacion.objects.all()
        # Utilizar el Serializador para convertir a una representación JSON
        # many=True indica que estamos serializando una lista de objetos
        serializer = HabitacionSerializers(habitacion, many=True)
        logger.info(f" Se consultó la lista de habitaciones ({len(habitacion)} encontradas).")  #len() función que se usa para obtener la cantidad de elementos de un objeto
        # Devolver la lista serializada como una respuesta JSON al cliente
        return Response(serializer.data)

  #PETICIÓN POST   → crea una nueva habitación
    def post(self, request):
        # Obtener los datos enviados por el cliente
        datos_peticion = request.data
        # Crear un serializador con esos datos
        serializer = HabitacionSerializers(data=datos_peticion)
        # Validar los datos recibidos
        if serializer.is_valid():
            # Si son válidos, guardar en la base de datos
            serializer.save()
            logger.info(f"Habitación creada : {serializer.data}")
            # Preparar la respuesta con los datos guardados
            respuesta = {
                'mensaje': 'Habitación creada exitosamente',
                'datos': serializer.data
            }
            # Devolver respuesta con código HTTP 201 (creado)
            return Response(respuesta, status=status.HTTP_201_CREATED)
        else:
            logger.warning(f"Error al crear habitación: {serializer.errors}")
            # Si no pasa la validación, devuelve los errores detectados
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HabitacionDetalleAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication] # Va a usar autenticación JWT para validar al usuario antes de permitir el acceso.
    # GET →devuelve una habitación específica
    def get(self, request, id_habitacion):
        logger.info(f"Se consultó la habitación ID={id_habitacion}.")
        # Ir a buscar en el modelo de habitación, el registro con pk=id_habitacion
        #Verificar si existe o no
         #Si existe debería rersponder con los datos serializados de habitacion
         #Si no existe debería responder con un error 404
          
        try:
            # SELECT * FROM Habitacion WHERE la primary key = id_habitacion
            habitacion = Habitacion.objects.get(pk=id_habitacion)
        except Habitacion.DoesNotExist:
            logger.error(f"Intento de acceder a habitación inexistente ID={id_habitacion}.")
            # Manejo del error si no se encuentra la habitación
            return Response({'error': 'Habitación no existente'}, status=status.HTTP_404_NOT_FOUND)

        # Si la habitación existe, se serializa y se retorna
        serializer = HabitacionSerializers(habitacion, context={'request': request})
        return Response(serializer.data)
       
       
       #Metodo DELETE para eliminar una habitación
    def delete(self, request, id_habitacion):
            # Ir a buscar en el modelo de habitación, el registro con pk=id_habitacion
            #Verificar si existe o no
            #Si existe debería rersponder con elimina la habitacion y reponder ok
            #Si no existe debería responder con un error 404

           try:
            # SELECT * FROM Habitacion WHERE la primary key = id_habitacion
            habitacion = Habitacion.objects.get(pk=id_habitacion)
           except Habitacion.DoesNotExist:
            logger.error(f"Intento de eliminar habitación inexistente ID={id_habitacion}.")
            # Manejo del error si no se encuentra la habitación
            return Response({'error': 'Habitación no existente'}, status=status.HTTP_404_NOT_FOUND)
        
        #DELETE FROM Habitacion WHERE primary_key=id_habitacion
           habitacion.delete()
           logger.warning(f"Habitación ID={id_habitacion} eliminada ")
           return Response({'mensaje':'La habitación fue eliminada con exito'},status=status.HTTP_204_NO_CONTENT)
    

     #Metodo PUT para actualizar los datos de las habitaciones
    def put (self, request,id_habitacion):
            # Ir a buscar en el modelo de habitación, el registro con pk=id_habitacion
            #Verificar si existe o no
            #Si existe , serializar los datos enviados en el cuerpo de la peticion
            #Verfico si hay error en la serializacion
            #Si es valido , actualizo la habitacion
            #Sino  respondo con los errores encontrados
            #Si no existe debería responder con un error 404
         try:
            # SELECT * FROM Habitacion WHERE la primary key = id_habitacion
            habitacion = Habitacion.objects.get(pk=id_habitacion)
         except Habitacion.DoesNotExist:
            logger.error(f"Intento de actualizar habitación inexistente ID={id_habitacion}.")
            # Manejo del error si no se encuentra la habitación
            return Response({'error': 'Habitación no existente'}, status=status.HTTP_404_NOT_FOUND)

         datos_peticion = request.data
         #Serializo
         serializer = HabitacionSerializers(habitacion,data=datos_peticion)
         if serializer.is_valid():
             #Si se cumple las validaciones guardo el registro habitacion
             serializer.save()
             logger.info(f"Habitación ID={id_habitacion} actualizada.")
             respuesta = {
                 'mensaje':'Habitación actualizada exitosamente',
                 'data' : serializer.data
             }
             return Response(respuesta) #por defecto el codigo de status es 200
         return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)



     # ---------------- RESERVAS ---------------- #

    # Gestiona peticiones GET para listar todas las reservas disponibles  y devuelve los datos en formato JSON al cliente.
class ReservaAPIView(APIView):
       #Get hara referencia a poder gestionar peticiones HTTP del tipo GET
       permission_classes = [IsAuthenticated] # Sólo usuarios autenticados pueden acceder
         # GET → devuelve una reserva por ID
       def get(self, request,id_reserva):
        try:
            reserva = Reserva.objects.get(pk=id_reserva)
        except Reserva.DoesNotExist:
            return Response({'error': 'Reserva no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ReservaReadSerializer(reserva)
        return Response(serializer.data)
        


from rest_framework .viewsets import ModelViewSet
from .serializers import HabitacionSerializers
from  .models import Habitacion


class HabitacionViewSet(ModelViewSet):
    #Especifico cual es serializador asociado
    serializer_class = HabitacionSerializers 
    #Devuelve todos los estudiantes
    queryset =  Habitacion.objects.all()



