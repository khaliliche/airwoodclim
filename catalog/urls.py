from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('climatiseurs/', views.product_list, {'category_type': 'climatiseur'}, name='climatiseurs'),
    path('services/', views.product_list, {'category_type': 'service'}, name='services'),
    path('produit/<slug:slug>/', views.product_detail, name='product_detail'),
]