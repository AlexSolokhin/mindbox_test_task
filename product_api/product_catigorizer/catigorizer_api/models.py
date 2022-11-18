from django.db import models


class Categories(models.Model):
    """
    Модель, описывающая категорию
    """

    name = models.CharField(verbose_name='категория', max_length=50)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return f'{self.name}'


class Goods(models.Model):
    """
    Модель, описывающая продукт
    """

    name = models.CharField(verbose_name='название', max_length=50)
    description = models.TextField(verbose_name='описание')
    categories = models.ManyToManyField(Categories, verbose_name='категории', blank=True)

    @property
    def short_description(self):
        return self.description[:30]

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    def __str__(self):
        return f'{self.name}'
