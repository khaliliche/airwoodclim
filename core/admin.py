from django.contrib import admin
from .models import WorkPhoto


@admin.register(WorkPhoto)
class WorkPhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'caption', 'order', 'is_active', 'created_at']
    list_editable = ['order', 'is_active']