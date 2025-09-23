from rest_framework import serializers
from.models import Habitacion , Reserva


# Serializador para el modelo Habitacion
class HabitacionSerializers(serializers.ModelSerializer):
    imagen = serializers.ImageField(use_url=True) # Devuelve la URL completa
    class Meta:
         #Relaciono al serializador con el modelo correspondiente
        model = Habitacion
        #Campos que quiero serializar del modelo
        fields= '__all__'
        #fields = ['titulo','precio','cantidad_personas','estado','descripcion']
    

    #VALIDACIONES PERSONALIZADAS DE LOS CAMPOS

    #Validación para el precio
    def validate_precio(self, value):
     if value < 0:
        # Lanzar una excepción indicando el error que quiero controlar
        raise serializers.ValidationError('El precio no puede ser negativo')
     return value

    #Validación para cantidad de personas
    def validate_cantidad_personas(self, value):
        if value <= 0:
            raise serializers.ValidationError('La cantidad de personas debe ser mayor a cero')
        return value

    #Validación para el titulo
    def validate_titulo(self, value):
        if value == "" :
            raise serializers.ValidationError('El título no puede estar vacío')
        return value


# Serializador para mostrar datos de una reserva
class ReservaReadSerializer(serializers.ModelSerializer):
    habitacion = HabitacionSerializers(read_only=True)  # Anidar datos de la habitación

    class Meta:
        #Relaciono al serializador con el modelo correspondiente
        model = Reserva
        #Campos que quiero serializar del modelo
        fields = [ 'nombre','telefono','email','fecha_entrada', 'fecha_salida','cantidad_personas' , 'habitacion']

        