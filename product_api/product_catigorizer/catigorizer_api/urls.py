from django.urls import path
from catigorizer_api.api import GoodsApiListView, CategoriesApiListView, RelationshipsApiView

urlpatterns = [
    path('goods', GoodsApiListView.as_view(), name='goods_api'),
    path('categories', CategoriesApiListView.as_view(), name='categories_api'),
    path('relations', RelationshipsApiView.as_view(), name='relations')
]
