from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator


class Catalog(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    # product = models.ForeignKey('Product', related_name='product', on_delete=models.CASCADE, verbose_name='商品',
    #                             null=True)

    class Meta:
        ordering = ['created_time']

    def __str__(self):
        return self.name


class Product(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    catalog = models.ForeignKey(Catalog, related_name='products', on_delete=models.CASCADE, verbose_name='类别', null=True)
    status = models.CharField(max_length=50, default='待提交')
    SKU = models.CharField(max_length=100, primary_key=True)
    owner = models.ForeignKey('auth.User', related_name='products', on_delete=models.CASCADE, verbose_name='开发人员')
    # owner = models.CharField(max_length=50, verbose_name='开发人员')
    title_en = models.CharField(max_length=200, verbose_name='标题英文')
    title_cn = models.CharField(max_length=200, verbose_name='标题中文')
    keyword = models.CharField(max_length=200, verbose_name='产品关键字')
    bought_price = models.DecimalField(verbose_name='采购价格', max_digits=9, decimal_places=2,
                                       validators=[MinValueValidator(Decimal('0.01'))])
    sell_price = models.DecimalField(verbose_name='销售价格', max_digits=9, decimal_places=2,
                                     validators=[MinValueValidator(Decimal('0.01'))])
    color = models.CharField(max_length=100, verbose_name='颜色', blank=True, null=True)
    size = models.CharField(max_length=100, verbose_name='尺寸', blank=True, null=True)
    style = models.CharField(max_length=100, verbose_name='风格', blank=True, null=True)
    amount = models.PositiveIntegerField(verbose_name='数量')
    material = models.CharField(max_length=100, verbose_name='材质', blank=True, null=True)
    desc = models.CharField(max_length=500, verbose_name='产品描述', blank=True, null=True)
    trans_method = models.CharField(max_length=100, verbose_name='运输', blank=True, null=True)
    trans_price = models.DecimalField(verbose_name='运费', max_digits=9, decimal_places=2,
                                      validators=[MinValueValidator(Decimal('0.01'))])
    pic_main = models.ImageField(verbose_name='主图', upload_to='images')
    pic_1st = models.ImageField(verbose_name='图片1', upload_to='images', blank=True, null=True)
    pic_2nd = models.ImageField(verbose_name='图片2', upload_to='images', blank=True, null=True)
    pic_3rd = models.ImageField(verbose_name='图片3', upload_to='images', blank=True, null=True)
    pic_4th = models.ImageField(verbose_name='图片4', upload_to='images', blank=True, null=True)
    pic_5th = models.ImageField(verbose_name='图片5', upload_to='images', blank=True, null=True)
    pic_6th = models.ImageField(verbose_name='图片6', upload_to='images', blank=True, null=True)
    pic_7th = models.ImageField(verbose_name='图片7', upload_to='images', blank=True, null=True)
    pic_8th = models.ImageField(verbose_name='图片8', upload_to='images', blank=True, null=True)

    product_weight = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='产品重量(克)',
                                         validators=[MinValueValidator(Decimal('0.01'))])
    package_weight = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='包装重量(克)',
                                         validators=[MinValueValidator(Decimal('0.01'))], blank=True, null=True)
    product_length = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='产品长(cm)',
                                         validators=[MinValueValidator(Decimal('0.01'))], blank=True, null=True)
    product_width = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='产品宽(cm)',
                                        validators=[MinValueValidator(Decimal('0.01'))], blank=True, null=True)
    product_high = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='产品高(cm)',
                                       validators=[MinValueValidator(Decimal('0.01'))], blank=True, null=True)
    product_link_1688 = models.CharField(max_length=200, verbose_name='产品1688链接')
    product_link_ebay = models.CharField(max_length=200, verbose_name='产品ebay链接', blank=True, null=True)
    product_link_amazon = models.CharField(max_length=200, verbose_name='产品Amazon链接', blank=True, null=True)
    product_link_speed_sell = models.CharField(max_length=200, verbose_name='产品速卖链接', blank=True, null=True)
    product_remarks = models.CharField(max_length=500, verbose_name='备注', blank=True, null=True)

    def __str__(self):
        return "{}  {}".format(self.title_cn, self.title_en)
