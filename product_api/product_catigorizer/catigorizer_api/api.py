from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from catigorizer_api.models import Goods, Categories
from catigorizer_api.serializers import GoodsSerializer, CategoriesSerializer


class GoodsApiListView(ListAPIView):
    """
    API продуктов
    """

    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer


class CategoriesApiListView(ListAPIView):
    """
    API категорий
    """

    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class RelationshipsApiView(APIView):
    """
    API таблицы отношений категорий к товарам
    """

    def get(self, request):

        relations_list = []
        goods = Goods.objects.all()
        for good in goods:
            goods_categories = good.categories.all()
            for category in goods_categories:
                relation_dict = {
                    'good_id': good.id,
                    'good_name': good.name,
                    'category_id': category.id,
                    'category_name': category.name,
                }
                relations_list.append(relation_dict)

        return Response(relations_list)
