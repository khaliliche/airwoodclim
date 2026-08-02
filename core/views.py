from django.shortcuts import render, redirect
from django.contrib import messages
from catalog.models import Product
from .models import WorkPhoto, Testimonial
from .forms import TestimonialForm


def home(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Merci pour votre avis ! Il sera visible après validation.")
            return redirect('core:home')
    else:
        form = TestimonialForm()

    climatiseurs = Product.objects.filter(category__type='climatiseur', is_active=True)[:4]
    services = Product.objects.filter(category__type='service', is_active=True)[:4]
    work_photos = WorkPhoto.objects.filter(is_active=True)[:8]
    testimonials = Testimonial.objects.filter(is_approved=True)[:9]

    return render(request, 'core/home.html', {
        'climatiseurs': climatiseurs,
        'services': services,
        'work_photos': work_photos,
        'testimonials': testimonials,
        'testimonial_form': form,
    })