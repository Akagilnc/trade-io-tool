from django.contrib.auth.models import User, Group
from rest_framework import serializers
from io_tool.models import Product, Catalog


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    catalog = serializers.ModelDurationField(verbose_name='分类')
    catalog_name = serializers.StringRelatedField(source='catalog')
    id = serializers.IntegerField(read_only=True)


    class Meta:
        model = Product
        fields = ('__all__')


class CatalogSerializer(serializers.ModelSerializer):
    products = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Catalog
        fields = ['id', 'name', 'url', 'products']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
