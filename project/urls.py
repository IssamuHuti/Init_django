"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

# quando faz chamada por requisição ao acessar um site, ela vai solicitar uma resposta para a chamada para exibir o resultado duma resquisição, que seria a resposta previamente estabelecida

# resposta previamente estabelecida
def home_view(request):
    print('outro texto') # resposta que será mostrada dentro do terminal
    return HttpResponse('HOME') # resposta para requisição de uma extensão com chamada dessa função

def blog_view(request):
    print('outro texto') # resposta que será mostrada dentro do terminal
    return HttpResponse('BLOG') # resposta para requisição de uma extensão com chamada dessa função


# requisição pelo site, mostrando a extensão do URL da página, e de onde que está sendo puxada a resposta da requisição
urlpatterns = [
    path('admin/', admin.site.urls), # URL utilizada para varidação da existencia do servidor, assim que for inserida outras URLs, esse site ficará indisponível, mesmo se apagar esse código após criarem outros caminhos não vai dar problema
    path('blog/', blog_view), # requisição requerida após o URL principal
    path('', home_view), # requisição requerida após o URL principal
]

# o que foi feito com def home_view e blog_view geralmente não acontece quando mexe com Django, geralmente no django é criada APPs para serem informadas dentro do arquivo settings.py

# assim digita-se no terminal python manage.py startapp nomedoAPP