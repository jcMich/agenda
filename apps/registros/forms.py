from django import forms
from .models import Registros, Grupos
from django.contrib.auth.models import User
from django.db.models import Q



class RegistrosForm(forms.ModelForm):
    def __init__(self,user,*args,**kwargs):
        super(RegistrosForm, self).__init__(*args,**kwargs)
        qs = Grupos.objects.filter(Q(user = User.objects.get(username = 'admin'))
                                   | Q(user = User.objects.get(username = user.username)))
        self.fields['grupo'].queryset = qs
        self.fields['grupo'].initial = Grupos.objects.get(pk=1)

    grupo = forms.ModelChoiceField(queryset=Registros.objects.none())
    class Meta:
        model = Registros
        exclude = {'user',}




class AddGrupoForm(forms.ModelForm):
    class Meta:
        model = Grupos
        exclude = {'user'}

    def clear_nombre(self):
        nombre = self.cleaned_data['nombre']
        try:
            r = Registros.objects.get(nombre=nombre)
        except r.DoesNotExist:
            return r
        raise forms.ValidationError("Este nombre de grupo ya existe")

