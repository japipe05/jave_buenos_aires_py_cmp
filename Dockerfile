# Usa una imagen base de Python
FROM python:3.11.0-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia solo los archivos necesarios para instalar las dependencias
COPY requirements.txt .

# Instala las dependencias del proyecto
RUN pip install -r requirements.txt

# Copia el resto de los archivos al directorio /app en el contenedor
COPY . .

# Set the environment variable to include /app in the Python path
ENV PYTHONPATH /app/src

# Comando para ejecutar la aplicación Flask
#CMD ["python", "src/app.py"]
CMD ["flask", "run", "--host=0.0.0.0"]
