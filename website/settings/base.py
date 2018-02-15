import environ

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
ROOT_DIR = environ.Path(__file__) - 2
# (website/settings/base.py - 3 = website/)
APPS_DIR = ROOT_DIR.path('website')
# Load operating system environment variables and then prepare to use them
env = environ.Env(DEBUG=(bool, False),)  # set default values and casting

env_file = str(ROOT_DIR.path('.env'))
env.read_env(env_file)

DEBUG = env('DEBUG')  # False if not in os.environ
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

SECRET_KEY = env('SECRET_KEY')
# Raises ImproperlyConfigured exception if SECRET_KEY not in os.environ

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
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# URL Configuration
# ----------------------------------------------------------------------------
ROOT_URLCONF = 'website.urls'

WSGI_APPLICATION = 'website.wsgi.application'


# DATABASE CONFIGURATION
# ----------------------------------------------------------------------------
DATABASES = {
    # 'default': env.db(),
    'default': env.db('SQLITE_URL', default='sqlite:///tmp/my-tmp-sqlite.db'),
    # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
    'extra': env.db('SQLITE_URL', default='sqlite:///tmp/my-tmp-sqlite.db')
}


# GENERAL CONFIGURATION
# ----------------------------------------------------------------------------
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1


# STATIC & MEDIA FILE CONFIGURATION
# ----------------------------------------------------------------------------

# PUBILC_DIR = ROOT_DIR.path()
MEDIA_ROOT = str(ROOT_DIR.path('media'))
MEDIA_URL = '/media/'
STATIC_ROOT = str(ROOT_DIR.path('staticfiles'))
STATIC_URL = '/static/'

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

# EMAIL CONFIGURATION
# ----------------------------------------------------------------------------

# FIXTURE CONFIGURATION
# ----------------------------------------------------------------------------

# MIGRATIONS CONFIGURATION
# ----------------------------------------------------------------------------

# Common stuff: Below this line define 3rd party library settings
# ----------------------------------------------------------------------------
