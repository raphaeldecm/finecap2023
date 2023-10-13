from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_stand_localizacao(value):
    """
    Validator for Stand name field.
    """
    if len(value) < 3:
        raise ValidationError(
            _('O campo "Localização" deve ter no mínimo 3 caracteres.'),
        )
    if len(value) > 10:
        raise ValidationError(
            _('O campo "Localização" deve ter no máximo 10 caracteres.'),
        )
