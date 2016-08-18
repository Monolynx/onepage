cd /vagrant_data/app
# project specific system packages
sudo pip3 install -r requirements.txt

echo "DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'app',
        'USER': 'app',
        'PASSWORD': 'app',
        'HOST': '',
        'PORT': '',
    }
}
ALLOWED_HOSTS = ['*']
DEBUG = True

TEMPLATE_DEBUG = DEBUG

THUMBNAIL_DEBUG = DEBUG

" > app/settings_local.py

python3 manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin1')" | python3 manage.py shell

echo "Superuser admin created with password 'admin1'"



