from django.shortcuts import render
# from django.http import HttpResponse


# Create your views here.
# tudo o que vai aparecer no site vai ser informada nesse arquivo

# descontinuidade por utilizar render
# def blog(request):
#     print('outro texto')
#     return HttpResponse('BLOG do APP')

# def exemplo(request):
#     print('exemplo 1')
#     return HttpResponse('EXEMPLO 1 do APP')

def blog(request):
    print('BLOG')
    return render(
        request,
        'blog.html',
    )

def exemplo(request):
    print('EXEMPLO')
    return render(
        request,
        'exemplo.html',
    )
