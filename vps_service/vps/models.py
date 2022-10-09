import uuid

from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class StatusType(models.TextChoices):
    ACTOR = 'started', _('Запущен')
    WRITER = 'blocked', _('Заблокирован')
    DIRECTOR = 'stopped', _('Остановлен')


class Vps(TimeStampedModel):
    uid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        primary_key=True
    )
    cpu = models.IntegerField(
        verbose_name=_('Количество ядер'),
        validators=[MinValueValidator(0)]
    )
    ram = models.IntegerField(
        verbose_name=_('объём RAM'),
        validators=[MinValueValidator(0)]
    )
    hdd = models.FloatField(
        verbose_name=_('объём HDD'),
        validators=[MinValueValidator(0)]
    )
    status = models.CharField(
        verbose_name=_('Статус сервера'),
        max_length=20,
        choices=StatusType.choices
    )

    class Meta:
        verbose_name = _('VPS')
        verbose_name_plural = _('VPS')
        db_table = "vps"
