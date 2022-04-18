
import django_filters

from .models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品的过滤类
    """
    pricemin = django_filters.NumberFilter(name='shop_price', help_text="最低价格",lookup_expr='gte')
    pricemax = django_filters.NumberFilter(name='shop_price', lookup_expr='lte')

    class Meta:
        model = Goods
        fields = ['pricemin', 'pricemax']
