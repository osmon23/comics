from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Comic(models.Model):
    """Модель Комиксов"""
    title = models.CharField(
        _('Title'),
        max_length=255,
    )
    author = models.CharField(
        _('Author'),
        max_length=255,
    )
    rating = models.DecimalField(
        _('Rating'),
        default=0,
        max_digits=3,
        decimal_places=2,
    )

    def __str__(self):
        return f'{self.title}: {self.rating}'

    class Meta:
        verbose_name = _('Comic')
        verbose_name_plural = _('Comics')


class Rating(models.Model):
    """Модель рейтинга комиксов"""
    comic_id = models.ForeignKey(
        Comic,
        on_delete=models.CASCADE,
        related_name='ratings',
        verbose_name=_('Comic'),
    )
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='ratings',
        verbose_name=_('User'),
    )
    VALUE = models.PositiveSmallIntegerField(
        _('Value'),
        choices=[(i, i) for i in range(1, 6)],
    )

    def __str__(self):
        return f'{self.user_id.username} gave {self.VALUE} to {self.comic_id.title}'

    class Meta:
        verbose_name = _('Rating')
        verbose_name_plural = _('Ratings')
