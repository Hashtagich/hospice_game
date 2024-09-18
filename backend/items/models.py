from django.db import models


# Create your models here.
class Resource(models.Model):
    title = models.CharField(
        max_length=250,
        verbose_name='Название',
    )

    quantity = models.IntegerField(
        verbose_name='Кол-во',
        default=1,
    )

    class Meta:
        verbose_name = 'Ресурс'
        verbose_name_plural = 'Ресурсы'
        ordering = ('-id',)

    def __str__(self):
        return self.title
