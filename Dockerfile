# Usa una imagen base de Python en Alpine
FROM python:3.9-alpine

# Instala las dependencias del sistema necesarias
RUN apk update && apk add --no-cache \
    libc-dev \
    gcc \
    libffi-dev \
    cairo-dev \
    pango-dev \
    jpeg-dev \
    zlib-dev \
    python3-dev \
    musl-dev \
    && rm -rf /var/cache/apk/*

# Configura el directorio de trabajo
WORKDIR /app

# Copia el archivo de requisitos
COPY requirements.txt /app/

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código del proyecto
COPY . /app/

# Asegúrate de que el script de entrada tiene permisos de ejecución
RUN chmod +x /app/entrypoint.sh

# Comando para ejecutar la aplicación en producción
CMD ["sh", "entrypoint.sh"]
