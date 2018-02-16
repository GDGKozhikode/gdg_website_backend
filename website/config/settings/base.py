import environ

ROOT_DIR = environ.Path(__file__) - 3
# (website/settings/base.py - 3 = website/)
APPS_DIR = ROOT_DIR.path('website')
# Load operating system environment variables and then prepare to use them
env = environ.Env(DEBUG=(bool, False),)  # set default values and casting

env_file = str(ROOT_DIR.path('.env'))
env.read_env(env_file)

# APP CONFIGURATION
# ----------------------------------------------------------------------------
CORE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'admin_interface',
    'flat_responsive',
    'colorfield',
]

PROJECT_APPS = [

]

INSTALLED_APPS = THIRD_PARTY_APPS + CORE_APPS + PROJECT_APPS

# MIDDLEWARE CONFIGURATION
# ----------------------------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# DEBUG
# ----------------------------------------------------------------------------
DEBUG = env.bool('DJANGO_DEBUG', False)

# TEMPLATE CONFIGURATION
# ----------------------------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            str(APPS_DIR.path('templates')),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# STATIC & MEDIA FILE CONFIGURATION
# ----------------------------------------------------------------------------

# PUBILC_DIR = ROOT_DIR.path()
MEDIA_ROOT = str(ROOT_DIR.path('media'))
MEDIA_URL = '/media/'
STATIC_ROOT = str(ROOT_DIR.path('staticfiles'))
STATIC_URL = '/static/'

# URL Configuration
# ----------------------------------------------------------------------------
ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

# EMAIL CONFIGURATION
# ----------------------------------------------------------------------------
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND',
                    default='django.core.mail.backends.smtp.EmailBackend')

# DATABASE CONFIGURATION
# ----------------------------------------------------------------------------
# Uses django-environ to accept uri format
DATABASES = {
    'default': env.db('DATABASE_URL', default='psql:///website'),
}
# DATABASES['default']['ATOMIC_REQUESTS'] = True


# GENERAL CONFIGURATION
# ----------------------------------------------------------------------------
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

# PASSWORD VALIDATION
# ----------------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# PASSWORD STORAGE SETTINGS
# ----------------------------------------------------------------------------

# AUTHENTICATION CONFIGURATION
# ----------------------------------------------------------------------------

# MANAGER CONFIGURATION
# ----------------------------------------------------------------------------

# FIXTURE CONFIGURATION
# ----------------------------------------------------------------------------

# MIGRATIONS CONFIGURATION
# ----------------------------------------------------------------------------

# Location of root django.contrib.admin URL, use {% url 'admin:index' %}
ADMIN_URL = r'^admin/'
# Common stuff: Below this line define 3rd party library settings
# ----------------------------------------------------------------------------
