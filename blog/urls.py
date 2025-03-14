from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog), # no modulo urls da de dentro da pasta project está informando que o que for adicionado aqui vai começar do 'blog/' informado no modulo da pasta project, pois a chamada do url blog começa a partir do 'blog/' da pasta project
    path('exemplo/', views.exemplo) # a extensão do url continua a partir do caminho principal deste documento, que no caso é o caminho vazio que representa 'blog/'
]
