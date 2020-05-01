# -*- coding:utf-8 -*-
import datetime
import os

import djcelery
from kombu import Queue, Exchange
from mongoengine import connect

djcelery.setup_loader()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=vrrozkxd_cec+6fk!%%-6z@0&7%z_4d0_o3$$dz1umwq#q+ko'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djcelery',
    'graphene_django',
    'rest_framework',
    'social_django',
    'user',
    'info',
    'blog',
    'avow',
    'order',
    'api'
)

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'red_travel.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'red_travel.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'travel',
        'USER': 'root',
        'PASSWORD': 'root123',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'OPTIONS': {
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}

MONGODB_DATABASES = {
    "default": {
        "name": "travel",
        "host": '127.0.0.1',
        "tz_aware": True,  # 设置时区
    },
}
connect('travel', host='127.0.0.1')

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        # 'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    )
}

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=3),
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'utils.JWT_Response_user.jwt_response_payload_handler',
}

# 使用redis保存session数据
ESSION_SAVE_EVERY_REQUEST = False  # 如果设置为True,django为每次request请求都保存session的内容，默认为False
SESSION_COOKIE_AGE = 60 * 60 * 24 * 3  # 设置SESSION的过期时间，单位是秒，默认是两周
SESSION_ENGINE = 'redis_sessions.session'  # 使用redis作为session存储介质
SESSION_REDIS_HOST = 'localhost'
SESSION_REDIS_PORT = 6379
SESSION_REDIS_DB = 0  # 选择存储槽
SESSION_REDIS_PASSWORD = ''
# SESSION_REDIS_PREFIX = 'session'

# CELERY STUFF
BROKER_URL = 'amqp://guest@localhost//'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/2'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_RESULT_EXPIRES = 24 * 60 * 60
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TIMEZONE = 'Asia/Shanghai'

CELERY_IMPORTS = ('user.tasks',)

CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
from datetime import timedelta

CELERYBEAT_SCHEDULE = {

    'request_to_chit_platform': {
        "task": "user.tasks.request_to_chit_platform",
        "schedule": timedelta(seconds=10),
        # "args": (),
    },
}

CELERY_QUEUES = (
    Queue(
        "default",
        Exchange("default"),
        routing_key="default"),
    Queue(
        "request_to_chit_platform",
        Exchange("request_to_chit_platform"),
        routing_key="request_to_chit_platform"),
)
CELERY_ROUTES = {
    'test_beat': {"queue": "default",
                  "routing_key": "default"},

    'request_to_chit_platform': {"queue": "request_to_chit_platform",
                                 "routing_key": "request_to_chit_platform"},
}
LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# 存静态文件
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# 存图片以及文件
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 第三方登录
# 设置要使用的第三方登录
AUTHENTICATION_BACKENDS = (
    'social_core.backends.weibo.WeiboOAuth2',  # 使用微博登录
    'social_core.backends.weixin.WeixinOAuth2',  # 使用微信登录
    'social_core.backends.qq.QQOAuth2',  # 使用QQ登录
    # 'django.contrib.auth.backends.ModelBackend',  # 指定django的ModelBackend类
    # 指定django的ModelBackend类为修改过的ModelBackend类
    'utils.JWT_Response_user.UsernameMobileAuthBackend'
)

# 配置微博开放平台授权
# SOCIAL_AUTH_要使用登录模块的名称大小_KEY，其他如QQ相同
SOCIAL_AUTH_QQ_KEY = '1107495796'  # QQ
SOCIAL_AUTH_QQ_SECRET = 'bda6GIebsi9QP3r96'  # QQ
SOCIAL_AUTH_QQ_USE_OPENID_AS_USERNAME = True
QQ_CALLBACK_URL = 'http://localhost:8000/oauth/qq_check'
# 登录成功后跳转页面
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/index/'
LOGIN_URL = '/purview/accounts/login/'
