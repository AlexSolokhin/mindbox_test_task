from rest_framework import serializers
from catigorizer_api.models import Goods, Categories


class GoodsSerializer(serializers.ModelSerializer):
    """
    Сериалайзер модели продуктов
    """

    class Meta:
        model = Goods
        fields = ['name', 'short_description', 'categories']
        depth = 1
        extra_kwargs = {'categories': {'required': False}}


class GoodsShortSerializer(serializers.ModelSerializer):
    """
    Сокращённый сериалайзер модели продуктов
    """

    class Meta:
        model = Goods
        fields = ['id', 'name']


class CategoriesSerializer(serializers.ModelSerializer):
    """
    Сериалайзер модели категорий
    """

    goods_set = GoodsShortSerializer(many=True, read_only=True)

    class Meta:
        model = Categories
        fields = ['name', 'goods_set']
        depth = 1
        extra_kwargs = {'goods': {'required': False}}




