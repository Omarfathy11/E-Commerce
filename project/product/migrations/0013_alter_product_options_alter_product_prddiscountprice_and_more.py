# Generated by Django 4.2.1 on 2023-07-25 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_alter_category_options_product_prddiscountprice'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDDiscountPrice',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name=' Discount Price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDISNew',
            field=models.BooleanField(default=True),
        ),
    ]
