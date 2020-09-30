from django.shortcuts import render

# Create your views here.


def index(request):
    context = {'curso': 'Aula de Django',
    'outro': 'Mais uma informação',
    'novamente': 'So pra fixar'}
    # return render(request, 'adminlte/index.html',context)
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')
