from .common import *
import dj_database_url

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Heroku specific
DATABASES ={
    'default':dj_database_url.config()
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'HOST': config('PDB_HOST'),
#         'NAME': config('PDB_NAME'),
#         'USER': config('PDB_USER'),
#         'PASSWORD': config('PDB_PASSWORD'),
#     }
# }
