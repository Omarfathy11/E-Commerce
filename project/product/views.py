from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
# Create your views here.

def product_list(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 3)  # Show  contacts per page.
    page = request.GET.get("page")
    product_list = paginator.get_page(page)
    context= {'product_list' : product_list }  #عشان يربطها باسمها الي في التيمبلت 
    return render(request, 'product/product_list.html', context)

def product_details(request, id):
    product_details  = Product.objects.get(id=id)
    context = {'product_details' : product_details}
    return render(request, 'product/product_details.html', context)