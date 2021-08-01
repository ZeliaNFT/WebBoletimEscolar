from django.shortcuts import render
from web.models import Aluno

# Create your views here.
def index(request):
    alunos = Aluno.objects.all()

    testeChave = {
        'alunos': alunos
    }
    return render(request, 'index.html',testeChave)


def aluno(request, id):
    aluno = Aluno.objects.get(id=id)
    context = {
        'aluno': aluno

    }
    return render(request, 'aluno.html',context)