from django.shortcuts import render
from catalog.models import Product
from .models import WorkPhoto


def home(request):
    climatiseurs = Product.objects.filter(category__type='climatiseur', is_active=True)[:4]
    services = Product.objects.filter(category__type='service', is_active=True)[:4]
    work_photos = WorkPhoto.objects.filter(is_active=True)[:8]
    return render(request, 'core/home.html', {
        'climatiseurs': climatiseurs,
        'services': services,
        'work_photos': work_photos,
    })