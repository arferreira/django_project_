import sys
import os

from django.conf import settings

DEBUG = os.environ.get('DEBUG', 'on') == 'on'
SECRET_KEY = os.environ.get('SECRET_KEY', '0@md%%&rk(g8%*b$8!y(i)g6_mzoxv1j-k%^qvz-p-cdkog%rz')
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
from django import forms
from django.conf.urls import url
from django.core.wsgi import get_wsgi_application
# import para a request
from django.http import HttpResponse, HttpResponseBadRequest

class ImageForm(forms.Form):
    """Formulário para validar o placeholder de imagem solicitado """
    height = forms.IntegerField(min_value=1, max_value=2000)
    width = forms.IntegerField(min_value=1, max_value=2000)

def placeholder(request, width, height):
    # TODO: O restante da view deverá ser inserido aqui
    form = ImageForm(
            {
                'height': height,
                'width': width
                }
            )
    if form.is_valid():
        height = form.cleaned_data['height']
        width = form.cleaned_data['width']
        # TODO: Gera a imagem do tamanho solicitado
        return HttpResponse('Ok')
    else:
        return HttpResponseBadRequest('Invalid Image Request')

def index(request):
    return HttpResponse('Hello World')

urlpatterns = (
        url(r'^image/(?P<width>[0-9]+)x(?P<height>[0-9]+)/$',
                                             placeholder, name='placeholder'),
        url(r'^$', index, name='homepage'),
        )


application = get_wsgi_application()

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
