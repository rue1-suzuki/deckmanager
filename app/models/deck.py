import os
from uuid import uuid4

from app.models import Event
from django.db import models
from django.db.models.deletion import CASCADE


def _image_upload_to(instance, filename):
    uuid = uuid4()
    (_, ext) = os.path.splitext(filename)
    new_name = f"{instance.number}_{instance.name}_{uuid}{ext}"
    return f"{instance.event.uuid}/{new_name}"


class Deck(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid4,
        verbose_name='デッキID',
    )

    event = models.ForeignKey(
        Event,
        on_delete=CASCADE,
        verbose_name='イベント',
    )

    number = models.IntegerField(
        verbose_name='識別番号',
    )

    name = models.CharField(
        max_length=128,
        verbose_name='ハンドルネーム',
    )

    image = models.ImageField(
        upload_to=_image_upload_to,
        verbose_name='デッキ画像',
    )

    remark = models.TextField(
        max_length=1024,
        null=True,
        blank=True,
        verbose_name='備考',
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='作成日時',
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='更新日時',
    )

    def __str__(self):
        return f"{self.event_id}_{self.number}-{self.name}"
