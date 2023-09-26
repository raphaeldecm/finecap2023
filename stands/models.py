from django.db import models
from django.utils.translation import gettext_lazy as _

from core.constants import (MAX_CHAR_FIELD_NAME_LENGTH,
                            MEDIUM_CHAR_FIELD_NAME_LENGTH,
                            SMALL_CHAR_FIELD_NAME_LENGTH)
from core.models import BaseModel


# Create your models here.
class Stand(BaseModel):

    localizacao = models.CharField(
        verbose_name=_("Localização"), max_length=SMALL_CHAR_FIELD_NAME_LENGTH
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
