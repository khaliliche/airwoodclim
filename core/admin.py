from django.contrib import admin
from .models import WorkPhoto, Testimonial


@admin.register(WorkPhoto)
class WorkPhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'caption', 'order', 'is_active', 'created_at']
    list_editable = ['order', 'is_active']


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'is_approved', 'created_at']
    list_editable = ['is_approved']
    list_filter = ['is_approved', 'rating']
    search_fields = ['name', 'comment']
    ordering = ['-created_at']