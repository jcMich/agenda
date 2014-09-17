__author__ = 'root'
from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    usuario = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))


class ContactForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput())
    titulo = forms.CharField(widget=forms.TextInput())
    comentario = forms.CharField(widget=forms.Textarea)

class RegistrarUsuarioForm(forms.Form):
    usuario = forms.CharField(widget=forms.TextInput())
    password_one = forms.CharField(widget=forms.PasswordInput(render_value=False))
    password_two = forms.CharField(widget=forms.PasswordInput(render_value=False))
    photo = forms.ImageField(required=False)

    def clean_usuario(self):
        usuario = self.cleaned_data['usuario']
        try:
            u = User.objects.get(username = usuario)
        except User.DoesNotExist:
            return usuario
        raise forms.ValidationError("Nombre de usuario ya existe")

    def clean_password_two(self):
        password_one = self.cleaned_data['password_one']
        password_two = self.cleaned_data['password_two']

        if password_one == password_two:
            pass
        else:
            raise forms.ValidationError("El password no coinsisde")
