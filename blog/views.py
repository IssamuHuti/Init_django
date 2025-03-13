# from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# tudo o que vai aparecer no site vai ser informada nesse arquivo

def blog(request):
    print('outro texto')
    return HttpResponse('BLOG do APP')