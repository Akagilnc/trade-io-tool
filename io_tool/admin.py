from django.contrib import admin
# from io_tool.models import Image
from django import forms
from .models import Product


# class ImageInline(admin.StackedInline):
#     model = Image
#     extra = 1


class ProductAdmin(admin.ModelAdmin):
    pass
    # inlines = [ImageInline]

    # def save_model(self, request, obj, form, change):
    #     obj.save()
    #
    #     for afile in request.FILES.getlist('photos_multiple'):
    #         print("saving pics")
    #         obj.images.create(file=afile)


admin.site.register(Product, ProductAdmin)