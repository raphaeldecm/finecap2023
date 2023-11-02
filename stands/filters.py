import django_filters
from django import forms

from .models import Stand


class StandFilter(django_filters.FilterSet):
    localizacao = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={
            "placeholder": "Localização do stand",
        })
    )
    valor = django_filters.CharFilter(
        widget=forms.TextInput(attrs={
            "class": "money",
            "placeholder": "Valor do stand",
        }),
        method='filter_valor',
    )

    def filter_valor(self, queryset, name, value):
        try:
            valor = float(value.replace(',', '.'))
        except ValueError:
            return queryset.none()

        return queryset.filter(**{f'{name}__exact': valor})

    class Meta:
        model = Stand
        fields = [
            'localizacao',
            'valor',
        ]
