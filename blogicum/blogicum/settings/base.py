from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = (
    'django-insecure-eoj*sn9+z+hk0wzrgqbts1!'
    'spgys$4+r4i+xsneo39)_kd)jx%'
)
DEBUG = False
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
]
LOGIN_REDIRECT_URL = '/profile/'
LOGOUT_REDIRECT_URL = '/'

ROOT_URLCONF = 'blogicum.urls'
WSGI_APPLICATION = 'blogicum.wsgi.application'

TEMPLATES_DIR = BASE_DIR / 'templates'

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = BASE_DIR / 'sent_emails'

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'NumericPasswordValidator',
    },
]