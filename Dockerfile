# Usa una imagen base oficial de Python
FROM python:3.8-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo requirements.txt
COPY requirements.txt /app/

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de la aplicación al contenedor
COPY src /app/src

# Define la variable de entorno para el Flask app
ENV FLASK_APP=/app/src/app.py

# Expone el puerto en el que corre Flask
EXPOSE 5000

# Comando por defecto para ejecutar la aplicación
CMD ["flask", "run", "--host=127.0.0.1", "--port=5000"]
