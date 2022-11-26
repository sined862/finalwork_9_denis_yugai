from django.db import models
from django.contrib.auth.models import User

class Photo(models.Model):
    img = models.ImageField(
        verbose_name='Фотография',
        upload_to='photos',
        null=False,
        blank=False
    )
    text = models.TextField(
        verbose_name='Подпись',
        max_length=500,
        null=False,
        blank=False
    )
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)
    author = models.ForeignKey(
        verbose_name='Автор резюме',
        to=User,
        related_name='photos',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    favorite = models.ManyToManyField(
        verbose_name='Избранные фото',
        to=User,
        related_name='favorites',
        null=True, 
        blank=True
    )

 


class Favorites(models.Model):
    author = models.ForeignKey(
        verbose_name='Автор резюме',
        to=User,
        related_name='favorited_author',
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    img = models.ForeignKey(
        verbose_name='Автор резюме',
        to=User,
        related_name='favorited_photos',
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.pk

