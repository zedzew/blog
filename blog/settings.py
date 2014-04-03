"""
Django settings for blog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'au$$r(r01(og!or_n)-3d+0@!gi-z4)7d6e=rp_3-1tqea1lc4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

TEMPLATE_DIRS = (
    'D:/pythonproject/PythonWeb/project/blog/templates',
    'D:/pythonproject/PythonWeb/project/blog/article/templates',
    'D:/pythonproject/PythonWeb/project/blog/loginsys/templates',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
##    'social_auth.context_processors.social_auth_by_name_backends',
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'article',
    'loginsys',
    'south',
    'disqus',
    'yandex_maps',
    'social_auth',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

DISQUS_API_KEY = 'BBx7FOJck2uyYnfQimaJzYd7J2c3fLV6tx0nNyVnFxlyEZwOrx5m2vdzOv7ifNM4'
DISQUS_WEBSITE_SHORTNAME = 'firstblogs'

YANDEX_MAPS_API_KEY = 'AGlQO1MBAAAAB3hhZAIAK6L0W72t-VQ_dXEHEJAhUiOVL7MAAAAAAAAAAABRQgGx6ctxEkGvjihgN02NZ92eIw=='

##GOOGLE_OAUTH2_CLIENT_ID = '452218904007.apps.googleusercontent.com'
##GOOGLE_OAUTH2_CLIENT_SECRET = 'XJi87TLiu6t36M0y6ceN-Lg2'

ROOT_URLCONF = 'blog.urls'

WSGI_APPLICATION = 'blog.wsgi.application'

##AUTHENTICATION_BACKENDS = (
##    'social_auth.backends.google.GoogleOAuth2Backend',
##)



# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'ru-Ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    ('static', 'D:/pythonproject/PythonWeb/project/blog/static'),
)



