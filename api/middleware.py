from django.utils.deprecation import MiddlewareMixin

class SimpleLoggingMiddleware(MiddlewareMixin):

    # Para contar cuántas veces se visita cada ruta
    contadores = {}

  # Método que se ejecuta antes de que Django procese la solicitud
    def process_request(self, request):
        # Guardamos el método HTTP de la petición
        metodo = request.method
         # Guardamos la ruta solicitada
        ruta = request.path
        # Obtenemos la IP del cliente, o un valor por defecto si no se encuentra
        ip = request.META.get('REMOTE_ADDR', 'IP desconocida')

    
        if ruta in self.contadores:
        # Incrementar contador de visitas por ruta
            self.contadores[ruta] += 1
        else:
            # Se inicializa contador de visita para una ruta
            self.contadores[ruta] = 1

       # Mostramos información de la petición en la consola
        print(f"Petición interceptada: [{metodo}] - {ruta} - IP: {ip}")
        print(f"{ruta} - Visitada {self.contadores[ruta]} veces")

        return None
    
    # Método que se ejecuta después de que Django genera la respuesta
    def process_response(self, request, response):
         # Guardamos el código de estado de la respuesta 
        status_code = response.status_code
        print(f"Respuesta capturada: {status_code}")

        #Agregar información a la cabecera de las respuestas
        response ['X-API-Name'] = 'San Remo API'
        response ['X-API-Version'] = '1.0'

     # Retornamos la respuesta para que se envíe al cliente
        return response
