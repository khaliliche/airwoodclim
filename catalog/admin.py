from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'slug']
    list_filter = ['type']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'brand', 'capacity_btu', 'price', 'is_active', 'created_at']
    list_filter = ['category', 'brand', 'is_active']
    list_editable = ['price', 'is_active']
    search_fields = ['name', 'brand', 'description']
    prepopulated_fields = {'slug': ('name',)}