from .base import *

DEBUG = False

# Allow all hosts — Railway domain is dynamic; restrict this once stable
ALLOWED_HOSTS = ["*"]

# Disable SSL redirect so Railway's proxy can handle HTTPS without redirect loops
SECURE_SSL_REDIRECT = False
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Static files handling via WhiteNoise for production
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
