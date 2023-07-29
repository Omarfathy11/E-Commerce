from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.

class Product(models.Model):
    PRDName = models.CharField(max_length=100, verbose_name=_("product name"))
    PRDCategory = models.ForeignKey('Category', on_delete=models.CASCADE,  blank=True, null=True)
    PRDBrand = models.ForeignKey('settings.Brand', on_delete=models.CASCADE, blank=True, null=True)
    PRDDesc = models.TextField(verbose_name=_("product description"), )
    PRDDImage = models.ImageField(upload_to='product/', verbose_name=_("image"), blank=True, null=True)    
    PRDPrice = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("Price")) # selling price 
    PRDDiscountPrice = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_(" Discount Price")) # selling price  
    PRDCost = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("Cost")) # The price at which you bought it
    PRDCreated = models.DateTimeField(verbose_name=("created at")) # time to created it automaticly
    PRDSlug = models.SlugField(blank=True, null=True, verbose_name=_("Product URL"))
    PRDISbestSeller = models.BooleanField(default=False, verbose_name=_("Best Seller"))
    PRDISNew = models.BooleanField(default=True, verbose_name=_("New Product "))
    


    def save(self, *args, **kwargs):
       if not self.PRDSlug:
         self.PRDSlug = slugify(self.PRDName)
       super(Product , self).save(*args, **kwargs) 

    class Meta:
      verbose_name  = _("Product")
      verbose_name_plural = _("Products")   

   
    def get_absolute_url(self):
       return reverse('products:product_detail',kwargs={'slug':self.PRDSlug})
    
    def __str__(self):
      return self.PRDName  # to show in administrasion
    
class ProduectImage(models.Model):
   PRDDIproduct = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("product"))
   PRDDIImage = models.ImageField(upload_to='product/', verbose_name=_("image"))    

   def __str__(self):
     return str(self.PRDDIproduct)   
   
class Category(models.Model):
   CatName = models.CharField(max_length=50, verbose_name=_("name"))
   CatParent = models.ForeignKey('self',limit_choices_to={'CatParent__isnull': True},verbose_name=_("main parent")  ,on_delete=models.CASCADE, blank=True, null=True)
   CatDes = models.TextField(verbose_name=_("Description"))
   CatImg = models.ImageField(upload_to="category", verbose_name=_("image"))

   class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


   def __str__(self):
      return self.CatName  # to show in administrasion

class product_Alternative(models.Model):
   PALNProduct = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="main_product", verbose_name=_("Product"))
   PALNAlternatives = models.ManyToManyField(Product, related_name="Alternative_Products", verbose_name=_("Alternatives"))

   class Meta:
      verbose_name  = _("Product Alernative")
      verbose_name_plural = _("Product Alernatives")

   def __str__(self):
      return str(self.PALNProduct)

    
class product_Accessories(models.Model):
   PACCProduct = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="mainAccessory_product", verbose_name=_("product"))
   PACCAlternatives = models.ManyToManyField(Product, related_name="Acscessories_Products", verbose_name=_("Accessories"))

   class Meta:
      verbose_name  = _("Product Accessory")
      verbose_name_plural = _("Product Acessories")

   def __str__(self):
      return str(self.PACCProduct)

     
    