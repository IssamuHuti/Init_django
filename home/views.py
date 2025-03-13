# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# tudo o que vai aparecer no site vai ser informada nesse arquivo

def home(request):
    print('outro texto')
    return HttpResponse('HOME do APP')