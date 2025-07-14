from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import CadastroForm, RecuperarSenhaForm
from .models import Usuario, Piscina, Monitoramento
import random
import string
from django.shortcuts import render, redirect
from django.shortcuts import render
from .models import Monitoramento
from .models import Monitoramento, Piscina
from .forms import MonitoramentoForm

class CustomPasswordResetView(PasswordResetView):
    template_name = 'sistema_piscina/recuperar_senha.html'
    success_url = reverse_lazy('login')


def index(request):
    return render(request, 'sistema_piscina/index.html')

def recuperar_senha(request):
    # Sua lógica de recuperação de senha aqui
    return render(request, 'recuperar_senha.html')

def cadastro_piscina(request):
    return render(request, 'sistema_piscina/cadastro_piscina.html')

def monitoramento(request):
    return render(request, 'sistema_piscina/monitoramento.html')

def pecas(request):
    return render(request, 'sistema_piscina/pecas.html')

def cadastro_equipamento(request):
    return render(request, 'sistema_piscina/cadastro_equipamento.html')

def recomendacoes(request):
    return render(request, 'sistema_piscina/recomendacoes.html')

@login_required
def dashboard(request):
    return render(request, 'sistema_piscina/dashboard.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        messages.error(request, 'Credenciais inválidas')
    return render(request, 'sistema_piscina/login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CadastroForm()
    return render(request, 'sistema_piscina/cadastro.html', {'form': form})

@login_required
def monitoramento_view(request):
    monitoramentos = Monitoramento.objects.all().order_by('-data_medicao')
    piscinas = Piscina.objects.all()
    return render(request, 'sistema_piscina/monitoramento.html', {
        'monitoramentos': monitoramentos,
        'piscinas': piscinas
    })





