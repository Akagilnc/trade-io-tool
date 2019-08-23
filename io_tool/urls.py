from django.urls import path, include
from rest_framework.routers import DefaultRouter
from io_tool import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'products', views.ProductViewSet, basename='products')

urlpatterns = [
    path('', include(router.urls)),
    path(r'get-current-user', views.current_user)
]
