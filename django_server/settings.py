import os
from django_server.shared_settings import *


ENV = os.getenv('ENV', 'dev')

if ENV.lower() == 'prod':
    SECRET_KEY = os.getenv('SECRET_KEY', 'SECRET')
    DEBUG = True

    from django_server.prod_settings import *
else:
    SECRET_KEY = os.getenv('SECRET_KEY', 'SECRET')
    DEBUG = True

    from django_server.dev_settings import *
