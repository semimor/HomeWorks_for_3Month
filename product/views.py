from django.shortcuts import render
from product.models import Product, Comment


# Create your views here.

def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        context = {
            'products': products
        }

        return render(request, 'products/products.html', context=context)


def product_detail_view(request, product_id):
    if request.method == 'GET':
        products = Product.objects.get(id=product_id)
        comments = Comment.objects.filter(products=products)

        context = {
            'products': products,
            'comments': comments
        }

        return render(request, 'products/detail.html', context=context)