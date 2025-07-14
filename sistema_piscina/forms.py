from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from .models import Usuario

class CadastroForm(UserCreationForm):
    nome_completo = forms.CharField(max_length=100, label='Nome Completo')
    email = forms.EmailField(label='E-mail')

    class Meta:
        model = Usuario
        fields = ('nome_completo', 'email', 'password1', 'password2')

    # Personalizando o rótulo de senha para uma melhor experiência
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Digite uma senha segura'}),
        label='Senha',
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirme sua senha'}),
        label='Confirmação de Senha',
    )

class RecuperarSenhaForm(PasswordResetForm):
    email = forms.EmailField(
        label="E-mail",
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email', 'placeholder': 'Digite seu e-mail cadastrado'})
    )
class MonitoramentoForm(forms.ModelForm):
    class Meta:
        model = Monitoramento
        fields = ['piscina', 'ph', 'temperatura']

