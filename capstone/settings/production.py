import os
from ..logging import *
from .base import *
from dotenv import load_dotenv
from pathlib import Path

# Cargar el archivo .env si existe
dotenv_path = Path.joinpath(BASE_DIR, '.env')
load_dotenv(dotenv_path)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

ALLOWED_HOSTS = ['proyectods2aerolinea.up.railway.app']
CSRF_TRUSTED_ORIGINS = ['proyectods2aerolinea.up.railway.app']

# Otras configuraciones
DEBUG = os.getenv('DEBUG', 'False') == 'True'
STATIC_ROOT = Path(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# Additional security settings
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')