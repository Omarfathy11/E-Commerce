# Generated by Django 4.2.1 on 2023-07-25 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_alter_product_prdslug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='PRDSlug',
            new_name='slug',
        ),
    ]
