from capstone.settings.base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=k3z-^1ov_hy5y%ebw(2e-npk@$#!(c8ix=+7so*hmw9m0c52*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')