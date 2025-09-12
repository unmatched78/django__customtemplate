# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# Convert DEBUG to boolean
DEBUG = os.getenv('DEBUG_STATE', 'False').lower() == 'true'

ALLOWED_HOSTS = ["*"]
