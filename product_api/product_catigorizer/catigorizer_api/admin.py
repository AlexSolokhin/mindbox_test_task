from django.contrib import admin
from catigorizer_api.models import Goods, Categories


@admin.register(Categories)
class MailingsAdmin(admin.ModelAdmin):
    """
    Регистрация и отображения модели Categories в админке
    """

    list_display = ['name']
    list_display_links = ['name']


@admin.register(Goods)
class MailingsAdmin(admin.ModelAdmin):
    """
    Регистрация и отображения модели Goods в админке
    """

    list_display = ['name', 'short_description']
    list_display_links = ['name']
    filter_horizontal = ['categories']
