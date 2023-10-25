import django_filters

from .models import Stand


class StandFilter(django_filters.FilterSet):
    localizacao = django_filters.CharFilter(lookup_expr='icontains')
    valor = django_filters.NumberFilter()

    class Meta:
        model = Stand
        fields = [
            'localizacao',
            'valor',
        ]
