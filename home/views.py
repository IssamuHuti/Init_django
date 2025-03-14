from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
# tudo o que vai aparecer no site vai ser informada nesse arquivo

# codigos abaixo são substituidas por códigos com return render, pois o render permite informar configuração de HTML e CSS
# def home(request):
#     print('outro texto')
#     return HttpResponse('HOME do APP')

# def exemplo(request):
#     print('exemplo 2')
#     return HttpResponse('EXEMPLO 2 do APP')

def home(request):
    print('HOME')
    
    return render(
        request,
        'home.html'
    )

