#encoding=utf-8
"""
Django settings for clusterdbm project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import logging.config
from django.core.urlresolvers import reverse_lazy
import pymysql  
pymysql.install_as_MySQLdb()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
SITE_BASE_URL = "/cdb"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = SITE_BASE_URL + "/media/"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=pas5c#eiy0*1qt9e*@*kqir6cc!r+bc^h81fe-hzurihg4+o+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['cloud.edroplet.com', 'edroplet.com']

CORS_ORIGIN_ALLOW_ALL = True
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django_admin_bootstrapped',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',

    'graphene_django',
    # for markdown
    'draceditor',
    
    # support https
    'werkzeug_debugger_runserver',
    'django_extensions',
    # support https DONE
    #Sentry 是一个实时事件日志记录和汇集的平台。其专注于错误监控以及提取一切事后处理所需信息而不依赖于麻烦的用户反馈。
    #'Sentry',
    
    'authtools',
    'crispy_forms',
    'easy_thumbnails',
    'tinymce',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'markdown_deux',
    'bootstrapform',
    'helpdesk',
    'django_tables2',
    'crudbuilder',

    'accounts',
    'profiles',
    'applications',
    'packages',
    'comments',
    'threadedcomments',
    'django_comments',
    'blog',
    'excel', 
]
# comment template
COMMENTS_APP = 'comments'

SITE_ID = 1

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'clusterdbm.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                 # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
                'django_settings_export.settings_export',
            ],
        },
    },
]

WSGI_APPLICATION = 'clusterdbm.wsgi.application'

#All settings that should be made accessible from templates need to be explicitly listed in settings.SETTINGS_EXPORT
GA_ID = 'UA-00000-0'
SETTINGS_EXPORT = [
        'STATIC_URL',
        'SITE_BASE_URL', 
]

#Now you can access those exported settings from your templates via settings.<KEY>:

#<!-- template.html -->

#{% if not settings.DEBUG %}
	#<script>ga('create', '{{ settings.GA_ID }}', 'auto');</script>
#{% endif %}

#If you wish to change the name of the context variable to something besides settings, add SETTINGS_EXPORT_VARIABLE_NAME = 'custom_name' to your settings.py. This is useful when some other plugin is already adding settings to your template contexts.
#FOO = 'bar'
#SETTINGS_EXPORT = ['FOO']
#SETTINGS_EXPORT_VARIABLE_NAME = 'my_config'
#<!-- template.html -->

#{{ my_config.FOO }}


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.mysql',
        # Or path to database file if using sqlite3.
        'NAME': 'cluster',
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'root',                  # Not used with sqlite3.
        # Set to empty string for localhost. Not used with sqlite3.
        'HOST': '127.0.0.1',
        # Set to empty string for default. Not used with sqlite3.
        'PORT': '3306',
        #'OPTIONS': {'init_command': 'SET storage_engine=INNODB;'}
    },
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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

# Show emails to console in DEBUG mode
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Log everything to the logs directory at the top
LOGFILE_ROOT = os.path.join(BASE_DIR, 'logs')

#Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

#ADMINS = [('taylor', 'taylor.h.dbm@gmail.com'),('huangqi','806749175@qq.com')]
ADMINS = ['xiaoshui', '114014232@qq.com']

EMAIL_HOST = 'mail.jucuyun.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'Taylor@jucuyun.com'
EMAIL_HOST_PASSWORD = 'TPUOErSQE8cJ'
DEFAULT_FROM_EMAIL = 'Taylor@jucuyun.com'
EMAIL_SUBJECT_PREFIX = '[jucuyun]'
#admin mail
SERVER_EMAIL = 'Taylor@jucuyun.com'

# Reset logging
LOGGING_CONFIG = None
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(pathname)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'proj_log_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOGFILE_ROOT, 'project.log'),
            'formatter': 'verbose'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'sql_log_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOGFILE_ROOT, 'sql.log'),
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'project': {
            'handlers': ['proj_log_file'],
            'level': 'DEBUG',
        },
        'sql_compute': {
            'handlers': ['sql_log_file'],
            'level': 'DEBUG',
        },
    }
}

logging.config.dictConfig(LOGGING)


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'
#LANGUAGE_CODE = 'zh_CN' #错误

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#PASSWORD VALIDIATION
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 6,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = SITE_BASE_URL + '/static/'
#STATIC_ROOT =os.path.join(BASE_DIR,'static')

# Authentication Settings
AUTH_USER_MODEL = 'authtools.User'
LOGIN_REDIRECT_URL = reverse_lazy("home")
LOGIN_URL = reverse_lazy("accounts:login")

CRISPY_TEMPLATE_PACK = 'bootstrap3'

THUMBNAIL_EXTENSION = 'png'     # Or any extn for your thumbnails

GRAPHENE = {
        'SCHEMA': 'clusterdbm.schema.schema'
}

#REST_FRAMEWORK
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
        ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        ),
}

CORS_ORIGIN_ALLOW_ALL = True

"""
Django contains a catch-all handler that displays exception information to the browser. When debugging with Wing, it is useful to also propagate these exceptions to the IDE. This can be done with a monkey patch as follows (for example, in local_settings.py on your development systems):
"""
import os
import sys

import django.views.debug

def wing_debug_hook(*args, **kwargs):
	if __debug__ and 'WINGDB_ACTIVE' in os.environ:
		exc_type, exc_value, traceback = sys.exc_info()
		sys.excepthook(exc_type, exc_value, traceback)
	return old_technical_500_response(*args, **kwargs)

old_technical_500_response = django.views.debug.technical_500_response
django.views.debug.technical_500_response = wing_debug_hook
#To enable debugging of Django templates, you will need to take the following two steps:
#(1_8.W001) The standalone TEMPLATE_* settings were deprecated in Django 1.8 and the TEMPLATES dictionary takes precedence. You must put the values of the following settings into your default TEMPLATES dict: TEMPLATE_DEBUG.
#TEMPLATE_DEBUG = True

# Global draceditor settings
# Input: string boolean, `true/false`

DRACEDITOR_ENABLE_CONFIGS = {
	'imgur': 'true',     # to enable/disable imgur/custom uploader.
	'mention': 'false',  # to enable/disable mention
	'jquery': 'true',    # to include/revoke jquery (require for admin default django)
}

# Imgur API Keys
#Please register application in https://api.imgur.com/oauth2/addclient to get IMGUR_CLIENT_ID and IMGUR_API_KEY.
DRACEDITOR_IMGUR_CLIENT_ID = 'your-client-id'
DRACEDITOR_IMGUR_API_KEY   = 'your-api-key'

# Safe Mode
DRACEDITOR_MARKDOWN_SAFE_MODE = True # default

# Markdownify
DRACEDITOR_MARKDOWNIFY_FUNCTION = 'draceditor.utils.markdownify' # default
DRACEDITOR_MARKDOWNIFY_URL = SITE_BASE_URL + '/draceditor/markdownify/' # default

# Markdown extensions (default)
DRACEDITOR_MARKDOWN_EXTENSIONS = [
        'markdown.extensions.extra',
    'markdown.extensions.nl2br',
    'markdown.extensions.smarty',
    'markdown.extensions.fenced_code',

    # Custom markdown extensions.
    'draceditor.extensions.urlize',
    'draceditor.extensions.del_ins', # ~~strikethrough~~ and ++underscores++
    'draceditor.extensions.mention', # require for mention
    'draceditor.extensions.emoji',   # require for emoji
]

# Markdown Extensions Configs
DRACEDITOR_MARKDOWN_EXTENSION_CONFIGS = {}

# Markdown urls
DRACEDITOR_UPLOAD_URL = SITE_BASE_URL + '/draceditor/uploader/' # default
DRACEDITOR_SEARCH_USERS_URL = SITE_BASE_URL + '/draceditor/search-user/' # default

# Markdown Extensions
DRACEDITOR_MARKDOWN_BASE_EMOJI_URL = 'https://assets-cdn.github.com/images/icons/emoji/' # default
DRACEDITOR_MARKDOWN_BASE_MENTION_URL = 'https://forum.dracos-linux.org/profile/' # default (change this)

# For django-excel
FILE_UPLOAD_HANDLERS = ("django_excel.ExcelMemoryFileUploadHandler",
                        "django_excel.TemporaryExcelFileUploadHandler")