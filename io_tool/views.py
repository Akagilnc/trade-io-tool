from django.contrib.auth.models import User, Group
from rest_framework import filters
from io_tool.models import Product, Catalog
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from io_tool.serializers import UserSerializer, GroupSerializer, ProductSerializer, CatalogSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q


@api_view(['GET'])
def current_user(request):
    user = request.user
    return Response({
        'username': user.username,
        'email': user.email,
        'groups': list(request.user.groups.values_list('name', flat=True))
    })


class CatalogViewSet(viewsets.ModelViewSet):
    """
    API endpoints that allows users to be viewed or edited
    """
    queryset = Catalog.objects.all().order_by('-created_time')
    serializer_class = CatalogSerializer
    pagination_class = None
    filter_backends = [filters.SearchFilter]
    # filter_fields = ['title_cn', 'title_en', 'SKU', 'owner', 'status']
    search_fields = ['name']


class ProductViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        catalog = self.request.query_params.get('catalog')
        status = self.request.query_params.get('status')
        group_names = self.request.user.groups.values_list('name', flat=True)
        if group_names:
            group_name = group_names[0].lower()
        else:
            group_name = None
        print(group_name)
        if group_name and group_name == 'dev':
            print(self.request.user)
            result = Product.objects.filter(owner=self.request.user).order_by('-created_time')
        else:
            result = Product.objects.all().order_by('-created_time')

        if group_name == 'dev':
            result = result.filter(Q(status='待提交') | Q(status='审核失败'))
        if group_name == 'ui':
            result = result.filter(status='审核通过')
        if group_name == 'sell':
            result = result.filter(status='已上线')

        if catalog:
            result = result.filter(catalog=catalog)
        if status and status != '':
            result = result.filter(status=status)

        return result

    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    # filter_fields = ['title_cn', 'title_en', 'SKU', 'owner', 'status']
    search_fields = ['SKU', 'title_cn', 'title_en', 'keyword', 'status']

    @action(detail=True, methods=['post'], name='Commit Product to UI', url_path='accept')
    def accept_product_ui(self, request, pk=None):
        product = self.get_object()
        product.status = '审核通过'
        product.save()
        return Response({'200': '产品已提交UI'})

    @action(detail=True, methods=['post'], name='Commit Product to admin', url_path='review')
    def commit_product_review(self, request, pk=None):
        product = self.get_object()
        product.status = '待审核'
        product.save()
        return Response({'200': '产品已提交审核'})

    @action(detail=True, methods=['post'], name='Accept Product to production', url_path='commit')
    def release_product(self, request, pk=None):
        product = self.get_object()
        product.status = '已上线'
        product.save()
        return Response({'200': '产品上线'})

    @action(detail=True, methods=['post'], name='Reject Product to dev', url_path='reject')
    def reject_product(self, request, pk=None):
        product = self.get_object()
        product.status = '审核失败'
        product.save()
        return Response({'200': '产品已拒绝'})

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoints that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoints that allows groups to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
