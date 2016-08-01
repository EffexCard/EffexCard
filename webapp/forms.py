# coding=utf-8
from django.forms import ModelForm
from webapp.models import *
from django import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput
from django.views.generic.edit import UpdateView
from django.template.loader import render_to_string
from datetime import date
from django.core.exceptions import ValidationError
from django.conf import settings
from django.contrib.auth import get_user_model

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        exclude=['user','foto']

class FotoForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ("foto",)

class CorreoForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ("email",)

class MiUserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ("email",)

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmación Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ("email",)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            msg = "Passwords don't match"
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class CompraForm(ModelForm):
    hidden_redirect = forms.CharField(widget=forms.HiddenInput(),initial="/compras")
    class Meta:
        model = Compra

    def clean(self):
        data = self.cleaned_data

        preciototal = self.cleaned_data.get('preciototal')
        cuenta = Cuenta.objects.filter(user=self.user)[0]
        if preciototal > cuenta.saldo:
            raise ValidationError("El precio total de la compra es mayor a su saldo")

        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CompraForm, self).__init__(*args, **kwargs)

class DepositoForm(ModelForm):
    hidden_redirect = forms.CharField(widget=forms.HiddenInput(),initial="/depositos")
    class Meta:
        model = Deposito
