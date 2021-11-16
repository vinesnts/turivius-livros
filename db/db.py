import os
import psycopg2

from dotenv import load_dotenv

# Loads enviroment variables from .env
load_dotenv()

DEBUG = os.environ.get('DEBUG') == "on"

DATABASES = {
    'default': {
        'NAME': os.environ.get('DB_NAME'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
    },
} if DEBUG else {
    'default': {
        'NAME': os.environ.get('DB_NAME_PROD'),
        'HOST': os.environ.get('DB_HOST_PROD'),
        'PORT': os.environ.get('DB_PORT_PROD'),
        'USER': os.environ.get('DB_USER_PROD'),
        'PASSWORD': os.environ.get('DB_PASSWORD_PROD'),
    }
}

def connect(database="default"):
    return psycopg2.connect(
        f"""dbname='{DATABASES[database]['NAME']}'
         user='{DATABASES[database]['USER']}'
         host='{DATABASES[database]['HOST']}' 
         port={DATABASES[database]['PORT']} 
         password='{DATABASES[database]['PASSWORD']}'""")