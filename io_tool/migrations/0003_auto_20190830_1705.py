# Generated by Django 2.2.4 on 2019-08-30 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('io_tool', '0002_auto_20190828_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='SKU',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
