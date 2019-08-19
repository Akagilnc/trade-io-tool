from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    SKU = models.CharField(max_length=100)
    owner = models.ForeignKey('auth.User', related_name='products', on_delete=models.CASCADE, verbose_name='开发人员')
    # owner = models.CharField(max_length=50, verbose_name='开发人员')
    title_en = models.CharField(max_length=200, verbose_name='标题英文')
    title_cn = models.CharField(max_length=200, verbose_name='标题中文')
    keyword = models.CharField(max_length=200, verbose_name='产品关键字')
    bought_price = models.DecimalField(verbose_name='采购价格', max_digits=9, decimal_places=2,
                                       validators=[MinValueValidator(Decimal('0.01'))])
    sell_price = models.DecimalField(verbose_name='销售价格', max_digits=9, decimal_places=2,
                                     validators=[MinValueValidator(Decimal('0.01'))])
    color = models.CharField(max_length=100, verbose_name='颜色')
    size = models.CharField(max_length=100, verbose_name='尺寸')
    style = models.CharField(max_length=100, verbose_name='风格')
    amount = models.PositiveIntegerField(verbose_name='数量')
    material = models.CharField(max_length=100, verbose_name='材质')
    desc = models.CharField(max_length=500, verbose_name='产品描述')
    trans_method = models.CharField(max_length=100, verbose_name='运输')
    trans_price = models.DecimalField(verbose_name='运费', max_digits=9, decimal_places=2,
                                      validators=[MinValueValidator(Decimal('0.01'))])
    pic_main = models.ImageField(verbose_name='主图', upload_to='images')
    pic_1st = models.ImageField(verbose_name='图片1', upload_to='images')
    pic_2nd = models.ImageField(verbose_name='图片2', upload_to='images')
    pic_3rd = models.ImageField(verbose_name='图片3', upload_to='images')
    pic_4th = models.ImageField(verbose_name='图片4', upload_to='images')
    pic_5th = models.ImageField(verbose_name='图片5', upload_to='images')
    pic_6th = models.ImageField(verbose_name='图片6', upload_to='images')
    pic_7th = models.ImageField(verbose_name='图片7', upload_to='images')
    pic_8th = models.ImageField(verbose_name='图片8', upload_to='images')
    # pic_main = models.CharField(verbose_name='主图地址', max_length=500)
    # pic_1st = models.CharField(verbose_name='图片1地址', max_length=500)
    # pic_2nd = models.CharField(verbose_name='图片2地址', max_length=500)
    # pic_3rd = models.CharField(verbose_name='图片3地址', max_length=500)
    # pic_4th = models.CharField(verbose_name='图片4地址', max_length=500)
    # pic_5th = models.CharField(verbose_name='图片5地址', max_length=500)
    # pic_6th = models.CharField(verbose_name='图片6地址', max_length=500)
    # pic_7th = models.CharField(verbose_name='图片7地址', max_length=500)
    # pic_8th = models.CharField(verbose_name='图片8地址', max_length=500)
    product_weight = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='产品重量',
                                         validators=[MinValueValidator(Decimal('0.01'))])
    package_weight = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='包装重量',
                                         validators=[MinValueValidator(Decimal('0.01'))])
    product_length = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='产品长(cm)',
                                         validators=[MinValueValidator(Decimal('0.01'))])
    product_width = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='产品宽(cm)',
                                        validators=[MinValueValidator(Decimal('0.01'))])
    product_high = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='产品高(cm)',
                                       validators=[MinValueValidator(Decimal('0.01'))])
    product_link_1688 = models.CharField(max_length=200, verbose_name='产品1688链接')
    product_link_ebay = models.CharField(max_length=200, verbose_name='产品ebay链接')
    product_link_amazon = models.CharField(max_length=200, verbose_name='产品Amazon链接')
    product_link_speed_sell = models.CharField(max_length=200, verbose_name='产品速卖链接')
    product_remarks = models.CharField(max_length=500, verbose_name='备注')

    def __str__(self):
        return "{} \n {}".format(self.title_cn, self.title_en)

# class Image(models.Model):
#     product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
#     file = models.ImageField(upload_to='images')
#     position = models.PositiveSmallIntegerField(default=0)
#
#     class Meta:
#         ordering = ['position']
#
#     def __str__(self):
#         return '{} -- {}'.format(self.product, self.file)
#
#     def save(self, *args, **kwargs):
#         print('handling pics')
#         print(self.file, type(self.file))
#
#         super(Image, self).save(*args, **kwargs)
