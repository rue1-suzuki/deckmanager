from datetime import date
from uuid import uuid4

from app.models import Organizer
from django.db import models
from django.db.models.deletion import CASCADE


class Event(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid4,
        verbose_name='イベントID',
    )

    organizer = models.ForeignKey(
        Organizer,
        on_delete=CASCADE,
        verbose_name='主催者',
    )

    title = models.CharField(
        max_length=128,
        verbose_name='イベント名',
    )

    date = models.DateField(
        default=date.today,
        verbose_name='開催日',
    )

    message = models.TextField(
        max_length=1024,
        null=True,
        blank=True,
        default='デッキ登録には\n・参加表明の番号\n・ハンドルネーム\n・デッキ画像\nの3つが必要です。',
        verbose_name='参加者へのメッセージ',
    )

    is_active = models.BooleanField(
        default=True,
        choices=(
            (True, '受付中'),
            (False, '受付終了'),
        ),
        verbose_name='状態',
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
        return f"{self.title}"
