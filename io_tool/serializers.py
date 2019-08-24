from django.contrib.auth.models import User, Group
from rest_framework import serializers
from io_tool.models import Product, Catalog


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # catalog = serializers.HyperlinkedRelatedField(many=False, view_name='catalog-detail', read_only=True)

    class Meta:
        model = Product
        fields = ('__all__')


class CatalogSerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='product-detail')

    class Meta:
        model = Catalog
        fields = ['name', 'url', 'products']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
