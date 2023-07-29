from .models import Product, ProduectImage
from django.contrib import admin

from product.models import ProduectImage , Category , product_Alternative, product_Accessories


admin.site.register(Product)
admin.site.register(ProduectImage)
admin.site.register(Category)
admin.site.register(product_Alternative)
admin.site.register(product_Accessories)