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

# Otras configuraciones
DEBUG = os.getenv('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')
STATIC_ROOT = Path(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"