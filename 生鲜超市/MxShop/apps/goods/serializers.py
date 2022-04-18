from rest_framework import serializers
from django.db.models import Q

from goods.models import Goods, GoodsCategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Goods
        fields = "__all__"
