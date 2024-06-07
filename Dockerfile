FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

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

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./capstone ./
COPY ./Data ./
COPY ./flight ./
COPY ./db.sqlite3 ./
COPY ./Dockerfile ./
COPY ./entrypoint.sh ./
COPY ./manage.py ./
COPY ./sonar-project.properties ./
CMD ["sh", "entrypoint.sh"]
