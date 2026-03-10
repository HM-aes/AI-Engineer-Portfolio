from .base import *

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# SQLite fallback for local if DATABASE_URL not in env, or override DATABASES explicitly
