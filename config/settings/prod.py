from .base import *

ALLOWED_HOSTS = ['43.202.175.207', 'areasj.store']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pybo',
        'USER': 'dbmasteruser',
        'PASSWORD':'sm1803hr!',
        'HOST': 'ls-fd0598da9bec1fbec48f244e35051fe129c9d6b2.ch9j4fdaqlmn.ap-northeast-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}
