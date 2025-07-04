from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView, LogoutView
from .forms import CadastroForm, RecuperarSenhaForm
from .models import Usuario
import random
import string
from django.contrib.auth import get_user_model  # Adicione esta importação
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Piscina


User = get_user_model()  

# Classe personalizada para redefinição de senha, se quiser customizar mais depois
class CustomPasswordResetView(PasswordResetView):
    pass

# Página inicial
def index(request):
    return render(request, 'sistema_piscina/index.html')

# Página de medições
def medicoes(request):
    return render(request, 'sistema_piscina/medicoes.html')

# Página do questionário
def questionario(request):
    return render(request, 'sistema_piscina/questionario.html')

# Página de cadastro
def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('index')  # ou 'dashboard' se houver
    else:
        form = CadastroForm()
    return render(request, 'sistema_piscina/cadastro.html', {'form': form})

# Página de login
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Alterado para redirecionar para o dashboard
        else:
            # Mensagem de erro se as credenciais estiverem incorretas
            return render(request, 'sistema_piscina/login.html', {
                'error': 'Usuário ou senha incorretos'
            })

    return render(request, 'sistema_piscina/login.html')

# Página de recuperação de senha
def recuperar_senha(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()  # Adicionado tratamento básico
        
        if not email:  # Verifica se o email está vazio
            messages.error(request, "Por favor, insira um e-mail válido.")
            return redirect('recuperar_senha')
        
        try:
            user = User.objects.get(email=email) 
            nova_senha = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            user.set_password(nova_senha)
            user.save()
            
            # EM PRODUÇÃO: Adicione aqui o envio por e-mail
            messages.success(request, f"Senha temporária gerada: {nova_senha}")
            return redirect('recuperar_senha')
            
        except User.DoesNotExist:
            messages.error(request, "E-mail não encontrado!")
        except Exception as e:
            messages.error(request, f"Erro inesperado: {str(e)}")

    return render(request, 'sistema_piscina/recuperar_senha.html')


@login_required
def pagina_view(request):
    return render(request, 'sistema_piscina/dashboard.html')

def cadastrar_usuario(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        if not email or not senha:
            messages.error(request, "E-mail e senha são obrigatórios!")
            return redirect('cadastrar_usuario')
        
        try:
            User.objects.create_user(
                username=email,
                email=email,
                password=senha
            )
            messages.success(request, "Cadastro realizado com sucesso!")
            return redirect('login')
        except Exception as e:
            messages.error(request, f"Erro ao cadastrar: {str(e)}")
            
    return render(request, 'sistema_piscina/cadastro.html')

def monitoramento(request):
    piscinas = Piscina.objects.all()
    return render(request, 'sistema_piscina/monitoramento.html', {'piscinas': piscinas})
@login_required
def cadastro_piscina_view(request):
    return render(request, 'sistema_piscina/cadastro_piscina.html')

@login_required
def pecas_view(request):
    return render(request, 'sistema_piscina/pecas.html')

@login_required
def cadastro_equipamento_view(request):
    return render(request, 'sistema_piscina/cadastro-equipamento.html')

@login_required
def recomendacoes_view(request):
    return render(request, 'sistema_piscina/recomendacoes.html')



