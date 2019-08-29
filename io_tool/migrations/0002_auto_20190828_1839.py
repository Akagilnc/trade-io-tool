# Generated by Django 2.2.4 on 2019-08-28 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('io_tool', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(blank=True, max_length=3000, null=True, verbose_name='产品描述'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_remarks',
            field=models.CharField(blank=True, max_length=3000, null=True, verbose_name='备注'),
        ),
    ]