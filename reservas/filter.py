import django_filters

from .models import Reserva


class ReservaFilter(django_filters.FilterSet):
    stand = django_filters.CharFilter(field_name='stand__localizacao', lookup_expr='icontains')

    class Meta:
        model = Reserva
        fields = ['stand']
