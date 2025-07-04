from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import recuperar_senha
from .views import recuperar_senha, pagina_view
from .views import cadastrar_usuario, login_view

urlpatterns = [
    # Páginas principais
    path('', views.login_view, name='index'),
    path('pagina/', views.pagina_view, name='pagina'),
    
    # Autenticação
    path('accounts/login/', views.login_view, name='login'),
    path('login/', views.login_view, name='login_alt'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastrar/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('recuperar-senha/', views.recuperar_senha, name='recuperar_senha'),
    
    # Funcionalidades do sistema
    path('medicoes/', views.medicoes, name='medicoes'),
    path('questionario/', views.questionario, name='questionario'),
    path('monitoramento/', views.monitoramento, name='monitoramento'),
    # Cadastros
    path('cadastro-piscina/', views.cadastro_piscina_view, name='cadastro_piscina'),
    path('cadastro-equipamento/', views.cadastro_equipamento_view, name='cadastro_equipamento'),
    
    path('pecas/', views.pecas_view, name='pecas'),
    path('recomendacoes/', views.recomendacoes_view, name='recomendacoes'),
]