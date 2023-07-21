from django.contrib import admin
from .models import Product, ProudectImage, Category, product_Alternative, product_Accessories
# Register your models here.
admin.site.register(Product)
admin.site.register(ProudectImage)
admin.site.register(Category)
admin.site.register(product_Alternative)
admin.site.register(product_Accessories)

