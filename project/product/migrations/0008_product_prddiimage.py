# Generated by Django 4.2.1 on 2023-07-19 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_product_prdbrand_product_prdcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PRDDIImage',
            field=models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='image'),
        ),
    ]
