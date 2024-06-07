# Usa la imagen base de Python
FROM python:3.9-slim

# Define variables de entorno
ENV PYTHONUNBUFFERED=1

# Establece el directorio de trabajo
WORKDIR /app

# Instala dependencias del sistema sin recomendaciones adicionales
RUN apt-get update && apt-get install -y \
    libcairo2 \
    libcairo2-dev \
    pkg-config \
    libffi-dev \
    libpango1.0-0 \
    libpangocairo-1.0-0 \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia los archivos de requerimientos y los instala
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copia los archivos del proyecto
COPY ./capstone ./
COPY ./Data ./
COPY ./flight ./
COPY ./db.sqlite3 ./
COPY ./Dockerfile ./
COPY ./entrypoint.sh ./
COPY ./manage.py ./
COPY ./sonar-project.properties ./

# Define el comando por defecto
CMD ["sh", "entrypoint.sh"]
