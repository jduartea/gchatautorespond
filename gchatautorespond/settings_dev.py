from .settings import *  # noqa

DEBUG = True
SECRET_KEY = 'dev_secret_key'
QUEUE_AUTH_KEY = 'dev_auth_key'

SCHEME = 'http://'
HOST = 'localhost'
ALLOWED_HOSTS = [HOST]
PORT = 8000

OAUTH_REDIRECT_URI = "%s%s:%s/%s" % (SCHEME, HOST, PORT, 'autorespond/oauth2callback/')

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'gchat_db.sqlite3')
    }
}

DJMAIL_REAL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
