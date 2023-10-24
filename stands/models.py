from core.constants import SMALL_CHAR_FIELD_NAME_LENGTH
from core.models import BaseModel
from django.db import models
from django.utils.translation import gettext_lazy as _
from stands.validators import validate_stand_localizacao


class Stand(BaseModel):

    localizacao = models.CharField(
        verbose_name=_("Localização"),
        max_length=SMALL_CHAR_FIELD_NAME_LENGTH,
    )
    valor = models.DecimalField(
        verbose_name=_("Valor"),
        decimal_places=2,
        max_digits=6
    )

    class Meta:
        verbose_name = _("Stand")
        verbose_name_plural = _("Stands")

    def __str__(self):
        return f"{self.pk} | {self.localizacao} | {self.valor}"
