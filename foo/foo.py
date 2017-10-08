import sys
import os

from django.conf import settings

DEBUG = os.environ.get('DEBUG', 'on') == 'on'
SECRET_KEY = os.environ.get('SECRET_KEY', 'g(9rt^z!kt4uk%kf2=btm$r^@d^u5%1kp3($y*t*3x#qre9z$q')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

settings.configure(
        DEBUG=DEBUG,
        SECRET_KEY=SECRET_KEY,
        ROOT_URLCONF=__name__,
        MIDDLEWARE_CLASSES=(
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.middleware.clickjacking.XFrameOptionsMiddleware',
            ),
        )

# import para as urls
from django.conf.urls import url
from django.core.wsgi import get_wsgi_application
# import para a request
from django.http import HttpResponse

def index(request):
    return HttpResponse('Antonio Ricardo')

urlpatterns = (
        url(r'^$', index),
        )

application = get_wsgi_application()

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
