import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = '8d&j_3zjc^4!)+3_s0!waya72jhx8j=3iryhexz=uq)9t)vbcs'

DEBUG = TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []

MIDDLEWARE_CLASSES = (
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
  'django.contrib.auth.context_processors.auth',
  'django.core.context_processors.debug',
  'django.core.context_processors.i18n',
  'django.core.context_processors.media',
  'django.core.context_processors.static',
  'django.core.context_processors.tz',
  'django.core.context_processors.request',
  'django.contrib.messages.context_processors.messages',
  'social.apps.django_app.context_processors.backends',
  'social.apps.django_app.context_processors.login_redirect',
)

ROOT_URLCONF = 'cando.main.urls'

WSGI_APPLICATION = 'main.wsgi.application'

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
  }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True = True = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '../.static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '../.media')
LOGIN_URL = '/auth/login/'
LOGIN_REDIRECT_URL = "/"

STATICFILES_FINDERS = (
  'django.contrib.staticfiles.finders.FileSystemFinder',
  'django.contrib.staticfiles.finders.AppDirectoriesFinder',
  # other finders..
  'compressor.finders.CompressorFinder',
)

LESS_EXECUTABLE = 'lessc'
COMPRESS_PRECOMPILERS = (('text/less', 'lessc {infile} {outfile}'),)

FAVICON = '/static/favicon.ico'

AUTHENTICATION_BACKENDS = (
  #'social.backends.open_id.OpenIdAuth',
  #'social.backends.google.GoogleOpenId',
  'social.backends.google.GoogleOAuth2',
  #'social.backends.google.GoogleOAuth',
  'social.backends.twitter.TwitterOAuth',
  #'social.backends.yahoo.YahooOpenId',
  'main.backends.EmailOrUsernameModelBackend',
  'django.contrib.auth.backends.ModelBackend',
)
