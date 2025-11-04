from rest_framework import serializers
from.models import Habitacion , Reserva
import re

#Funcion que verifica que el valor posee caracteres que no sean alfabeticos
def validar_caracteres_alfabeticos(value):
     if not re.match(r'[a-zA-Z \s] + $',value):
         raise serializers.ValidationError('El valor debe ser alfabetico')


# Serializador para el modelo Habitacion
class HabitacionSerializers(serializers.ModelSerializer):

    # VALIDACIÓN PERSONALIZADA PARA EL NOMBRE QUE SOLO CONTENGA CARACTERES ALFABETICOS
    nombre= serializers.CharField (
           max_length=100,
           #Se agregan a una lista las funciones que permiten hacer validaciones personalizadas
           validators = [validar_caracteres_alfabeticos]
    )

    imagen = serializers.ImageField(use_url=True) # Devuelve la URL completa
    class Meta:
         #Relaciono al serializador con el modelo correspondiente
        model = Habitacion
        #Campos que quiero serializar del modelo
        #fields= '__all__'
        #fields = ['titulo','precio','cantidad_personas','estado','descripcion']
        fields = ['nombre' , 'precio' ,'capacidad' , 'descripcion','estado', 'imagen']
    
 
    #----------------VALIDACIONES PERSONALIZADAS DE LOS CAMPOS-------------#

    #Validación para el precio
    def validate_precio(self, value):
     if value < 0:
        # Lanzar una excepción indicando el error que quiero controlar
        raise serializers.ValidationError('El precio no puede ser negativo')
     if value > 500000 :
         raise serializers.ValidationError('El precio no puede superar el $ 500.000')
     return value
 
    #Validación para cantidad de personas
    def validate_capacidad(self, value):
        if value <= 0:
            raise serializers.ValidationError('La cantidad de personas debe ser mayor a cero')
        if value > 6:
           raise serializers.ValidationError('La cantidad de personas no puede superar 6')
        return value
        
    #Validación para el titulo
    def validate_nombre(self, value):
        if value == "" :
            raise serializers.ValidationError('El nombre no puede estar vacío')
        if value > 100 :
            raise serializers.ValidationError('El nombre no puede superar 100 caracteres')
        if value < 5 :
            raise serializers.ValidationError('El nombre debe contener al menos 5 caracteres')
        
        return value
  # Validación para la descripción
    def validate_descripcion(self, value):
        if not value.strip():
            raise serializers.ValidationError('La descripción no puede estar vacía')
        if len(value) > 500:
            raise serializers.ValidationError('La descripción no puede superar los 500 caracteres')
        return value

# Serializador para mostrar datos de una reserva
class ReservaReadSerializer(serializers.ModelSerializer):
     
     # VALIDACIÓN PERSONALIZADA PARA EL NOMBRE QUE SOLO CONTENGA CARACTERES ALFABETICOS
    nombre= serializers.CharField (
            max_length=100,
           #Se agregan a una lista las funciones que permiten hacer validaciones personalizadas
           validators = [validar_caracteres_alfabeticos]
    )

    habitacion = HabitacionSerializers(read_only=True)  # Anidar datos de la habitación

    class Meta:
        #Relaciono al serializador con el modelo correspondiente
        model = Reserva
        #Campos que quiero serializar del modelo
        fields = [ 'nombre','telefono','email','fecha_entrada', 'fecha_salida','cantidad_personas' , 'habitacion']

        