from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def product_list(request, category_type):
    categories = Category.objects.filter(type=category_type)
    products = Product.objects.filter(category__type=category_type, is_active=True)

    brand = request.GET.get('brand')
    if brand:
        products = products.filter(brand__iexact=brand)

    brands = (
        Product.objects.filter(category__type=category_type, is_active=True)
        .exclude(brand='')
        .values_list('brand', flat=True)
        .distinct()
        .order_by('brand')
    )

    page_title = 'Climatiseurs' if category_type == 'climatiseur' else "Services d'installation"

    context = {
        'categories': categories,
        'products': products,
        'brands': brands,
        'selected_brand': brand,
        'category_type': category_type,
        'page_title': page_title,
    }
    return render(request, 'catalog/product_list.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, 'catalog/product_detail.html', {'product': product})