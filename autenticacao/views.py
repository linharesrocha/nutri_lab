from django.shortcuts import render, redirect
from .utils import password_is_valid
from django.http import HttpResponse

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not password_is_valid(request, senha, confirmar_senha):
            return redirect('/auth/cadastro/')
        
        return HttpResponse('Usuário cadastrado com sucesso!')

def logar(request):
    return render(request, 'cadastro.html')