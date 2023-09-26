from django import forms

from stands.models import Stand


class StandForm(forms.ModelForm):

    localizacao = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Localização do stand",
        })
    )
    valor = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Valor do stand",
        })
    )

    class Meta:
        model = Stand
        fields = (
            "localizacao",
            "valor",
        )
