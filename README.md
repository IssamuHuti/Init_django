Instalar Django

Iniciando o projeto Django
1 - Terminal: django-admin startproject project .
    * startproject = inicialia o projeto (só é utilizada quando não possui projeto django inicializada)
    * project = pasta que armazena todos os arquivos importantes para funcionamento do Django
    * * = todos os arquivos que são criadas com a inicialização serão criadas dentro da pasta Raiz, no caso a pasta DJANGO
1.2 - Terminal: django-admin startproject nomeDoProjeto
    * inicia um projeto criando uma pasta 'nomeDoProjeto' e dentro dela tem outra pasta com o mesmo nome e o restante dos arquivos

2 - Terminal: python manage.py runserver
    * verifica se foi criado a pasta corretamente para criação de site
    * runserver = sobe o arquivo no servidor
    * manage.py = arquivo django criado no passo 1
    * clicar em cima do servidor informado para verificar se deu certo "http://...." selecionando Ctrl
    * a cada atualização no site, no terminal será feita uma atualização
    * Ctrl + C para para o servidor


Função dos arquivos dentro da pasta criada na inicialização do Django
1 - settings.py
    * informa todas as configurações para executar o programa django e onde salvar o arquivo
2 - urls.py
    * informa o endereço dos servidores, podendo informar o url principal ou adjacentes 

Comandos uteis
django-admin == manage.py (manage.py é criada após executar o startproject)
1 - django-admin --help
    * utilizada para consultar funções que está disponível para configurar ou criar o projeto django
    * startproject é uma das funções que inicializa um projeto do zero, é e a única função que é utilizado antes da criação do projeto
2 - runserver
    * inicializada o servidor para rodar o site
3 - startapp
    * cria uma pasta para uma função que retorna uma HttpResponse
    * na pasta as funções que foram criadas no urls.py vai ser duplicado para nova pasta