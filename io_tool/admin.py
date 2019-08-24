from django.contrib import admin
# from io_tool.models import Image
from django import forms
from .models import Product, Catalog


# class ImageInline(admin.StackedInline):
#     model = Image
#     extra = 1


class ProductAdmin(admin.ModelAdmin):
    pass


class CatalogAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
admin.site.register(Catalog, CatalogAdmin)
