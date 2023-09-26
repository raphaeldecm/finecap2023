from django import forms

from core.widgets import GovbrSelect
from reservas.models import Reserva
from stands.models import Stand


class ReservaForm(forms.ModelForm):

    cnpj_empresa = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "CNPJ da empresa",
        })
    )
    nome_empresa = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Nome da empresa",
        })
    )
    email_empresa = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Email da empresa",
        })
    )
    categoria_empresa = forms.ChoiceField(
        choices=Reserva.Categoria.choices,
        label="Cetagoria",
        widget=GovbrSelect,
    )
    quitado = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            "class": "form-control",
        })
    )
    stand = forms.ModelChoiceField(
        queryset=Stand.objects.all(),
        label="Stand",
        required=True,
        widget=GovbrSelect,
    )

    class Meta:
        model = Reserva
        fields = (
            "cnpj_empresa",
            "nome_empresa",
            "email_empresa",
            "categoria_empresa",
            "quitado",
            "stand",
        )
