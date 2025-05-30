# Standard Python imports
import os
from pathlib import Path
from datetime import timedelta

# Load environment variables from .env file
from dotenv import load_dotenv

# Optional: Use python-decouple to manage environment configs
from decouple import config

# Define the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Load .env file located at the project root
load_dotenv(os.path.join(BASE_DIR, '.env'))

# SECURITY WARNING: keep the secret key used in production secret!
# Load it from the .env file for safety
SECRET_KEY = config('SECRET_KEY', default='your-fallback-secret-key')

# Enable debug mode — set to False in production!
DEBUG = True

# Allow requests only from localhost (set this for security in production)
ALLOWED_HOSTS = []

# Django apps that are always needed
INSTALLED_APPS = [
    'django.contrib.admin',           # Admin dashboard
    'django.contrib.auth',            # User authentication system
    'django.contrib.contenttypes',    # Handles model content types
    'django.contrib.sessions',        # Session management
    'django.contrib.messages',        # Messaging framework
    'django.contrib.staticfiles',     # Static file support

    # Third-party apps
    'rest_framework',                 # Django REST Framework
    'rest_framework.authtoken',       # Token authentication
    'dj_rest_auth',                   # REST endpoints for login/logout/registration
    'allauth',                        # Core django-allauth
    'allauth.account',                # Account management (sign up, login)
    'allauth.socialaccount',          # Social account support
    'allauth.socialaccount.providers.google',  # Google OAuth2 provider

    # Local apps
    'orders',                         # Custom app for managing orders
]

# Middleware handles request/response processing
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Basic security
    'django.contrib.sessions.middleware.SessionMiddleware',  # Session handling
    'django.middleware.common.CommonMiddleware',  # General request/response handling
    'django.middleware.csrf.CsrfViewMiddleware',  # Cross-site request forgery protection
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Attach user to requests
    'allauth.account.middleware.AccountMiddleware',  # Required for allauth's session state
    'django.contrib.messages.middleware.MessageMiddleware',  # Flash messages
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Prevent clickjacking
]

# Main URL configuration
ROOT_URLCONF = 'order_management.urls'

# Templating engine setup
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # You can add custom HTML template folders here
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',      # Add debug info to templates
                'django.template.context_processors.request',    # Required by allauth
                'django.contrib.auth.context_processors.auth',   # Adds user to templates
                'django.contrib.messages.context_processors.messages',  # Adds messages
            ],
        },
    },
]

# WSGI app entry point (used in production deployment)
WSGI_APPLICATION = 'order_management.wsgi.application'

# Default database setup using SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation rules
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JS, images) URL
STATIC_URL = '/static/'

# Required for django-allauth: identify which site this is (Site object in admin panel)
SITE_ID = 1

# Google OAuth configuration for django-allauth
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email'],  # What data we request from Google
        'AUTH_PARAMS': {'access_type': 'online'},  # No refresh token
        'VERIFIED_EMAIL': True,  # Require verified emails from Google
    }
}

# Django REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',  # Use JWT stored in cookies
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',  # Require login by default
    ),
}

# Simple JWT settings (used with dj-rest-auth)
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),     # 1 hour token validity
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),     # 1 week refresh token
    'ROTATE_REFRESH_TOKENS': True,                   # Issue new refresh token after login
    'BLACKLIST_AFTER_ROTATION': True,                # Prevent reuse of old refresh tokens
    'AUTH_HEADER_TYPES': ('Bearer',),                # Token format: Bearer <token>
}

# Redirect after successful login (you can change this to a dashboard)
LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'

# Securely load Google OAuth credentials from .env file
GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
