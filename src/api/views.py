
from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse
from rest_framework.views import APIView
from .models import Habitacion , Reserva
from .serializers import HabitacionSerealizers , ReservaReadSerializer
from rest_framework.response import Response 
from rest_framework import status


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
    

class HabitacionAPIView(APIView):

    #PETICIÓN GET 
    #Obtenemos todas las habitaciones
    def get(self, request):
        # Voy a buscar las habitaciones en mi base de datos 
        habitacion = Habitacion.objects.all()
        # Utilizar el Serializador para convertir a una representación JSON
        # many=True indica que estamos serializando una lista de objetos
        serializer = HabitacionSerealizers(habitacion, many=True)
        # Devolver la lista serializada como una respuesta JSON al cliente
        return Response(serializer.data)
  
  #PETICIÓN POST
    def post(self, request):
        # Obtener los datos enviados por el cliente
        datos_peticion = request.data
        # Crear un serializador con esos datos
        serializer = HabitacionSerealizers(data=datos_peticion)
        # Validar los datos recibidos
        if serializer.is_valid():
            # Si son válidos, guardar en la base de datos
            serializer.save()
            # Preparar la respuesta con los datos guardados
            respuesta = {
                'mensaje': 'Habitación creada exitosamente',
                'datos': serializer.data
            }
            # Devolver respuesta con código HTTP 201 (creado)
            return Response(respuesta, status=status.HTTP_201_CREATED)
        else:
            # Si no pasa la validación, devuelve los errores detectados
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HabitacionDetalleAPIView(APIView):
    def get(self, request, id_habitacion):
        # Ir a buscar en el modelo de habitación, el registro con pk=id_habitacion
        #Verificar si existe o no
         #Si existe debería rersponder con los datos serializados de habitacion
         #Si no existe debería responder con un error 404
          
        try:
            # SELECT * FROM Habitacion WHERE la primary key = id_habitacion
            habitacion = Habitacion.objects.get(pk=id_habitacion)
        except Habitacion.DoesNotExist:
            # Manejo del error si no se encuentra la habitación
            return Response({'error': 'Habitación no existente'}, status=status.HTTP_404_NOT_FOUND)

        # Si la habitación existe, se serializa y se retorna
        serializer = HabitacionSerealizers(habitacion)
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
            # Manejo del error si no se encuentra la habitación
            return Response({'error': 'Habitación no existente'}, status=status.HTTP_404_NOT_FOUND)
        
        #DELETE FROM Habitacion WHERE primary_key=id_habitacion
           habitacion.delete()
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
            # Manejo del error si no se encuentra la habitación
            return Response({'error': 'Habitación no existente'}, status=status.HTTP_404_NOT_FOUND)

         datos_peticion = request.data
         #Serializo
         serialaizer = HabitacionSerealizers(habitacion,data=datos_peticion)
         if serialaizer.is_valid():
             #Si se cumple las validaciones guardo el registro habitacion
             serialaizer.save()
             respuesta = {
                 'mensaje':'Habitación actualizada exitosamente',
                 'data' : serialaizer.data
             }
             return Response(respuesta) #por defecto el codigo de status es 200
         return Response (serialaizer.errors,status=status.HTTP_400_BAD_REQUEST)



     
    # Gestiona peticiones GET para listar todas las reservas disponibles  y devuelve los datos en formato JSON al cliente.
class ReservaAPIView(APIView):
       #Get hara referencia a poder gestionar peticiones HTTP del tipo GET
       def get(self, request,id_reserva):
        try:
            reserva = Reserva.objects.get(pk=id_reserva)
        except Reserva.DoesNotExist:
            return Response({'error': 'Reserva no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ReservaReadSerializer(reserva)
        return Response(serializer.data)
        
