from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = (
    'django-insecure-eoj*sn9+z+hk0wzrgqbts1!'
    'spgys$4+r4i+xsneo39)_kd)jx%'
)
DEBUG = True
ALLOWED_HOSTS = []

ROOT_URLCONF = 'blogicum.urls'
WSGI_APPLICATION = 'blogicum.wsgi.application'

LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
