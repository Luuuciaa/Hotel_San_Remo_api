# -------------------------------
# Dockerfile para Hotel San Remo API
# -------------------------------

# Paso 1: Imagen base y directorio de trabajo
FROM python:3.12-slim
 #Paso 2: 
WORKDIR /app

# Paso 3: Instalar dependencias del sistema necesarias para mysqlclient
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    libssl-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Paso 4: Copiar requirements.txt y actualizar pip
COPY requirements.txt .
RUN pip install --upgrade pip

# Paso 5: Instalar dependencias de Python (incluye python-dotenv, mysqlclient, Django, etc.)
RUN pip install -r requirements.txt

# Paso 6: Copiar el resto del proyecto
COPY . .

# Paso 7: Exponer puerto y comando por defecto
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
