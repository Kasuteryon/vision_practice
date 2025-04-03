FROM python:3.12.4-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /backend

# Copia el archivo de dependencias
COPY /backend/requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de tu aplicación
COPY /backend/enlaces.py .

# Comando de inicio
CMD ["python", "enlaces.py"]