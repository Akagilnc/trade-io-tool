from django.shortcuts import render
from django.contrib.auth.models import User, Group
from io_tool.models import Product
from rest_framework import viewsets, permissions
from io_tool.serializers import UserSerializer, GroupSerializer, ProductSerializer
from .forms import UploadFileForm
from django.http import HttpResponseRedirect


def handle_uploaded_file(f):
    with open('./name.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            print('handling pic')
            destination.write(chunk)


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['photos_multiple'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, "upload.html", {'form': form})


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAuthenticated]

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
