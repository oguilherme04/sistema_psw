from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from .views import (
    index, dashboard, login_view, logout_view, cadastro,
)

app_name = 'sistema_piscina' 

urlpatterns = [
    path('', views.index, name='index'), 
    path('recuperar-senha/', views.recuperar_senha, name='recuperar_senha'),
    path('cadastro-piscina/', views.cadastro_piscina, name='cadastro_piscina'),
    path('monitoramento/', views.monitoramento, name='monitoramento'),
    path('pecas/', views.pecas, name='pecas'),
    path('cadastro-equipamento/', views.cadastro_equipamento, name='cadastro_equipamento'),
    path('recomendacoes/', views.recomendacoes, name='recomendacoes'),
    path('dashboard/', dashboard, name='dashboard'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('cadastro/', cadastro, name='cadastro'),
    path('reset-password/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('monitoramento/', monitoramento_view, name='monitoramento'),
    path('monitoramento/novo/', nova_medicao, name='nova_medicao'),
]
