# items/admin.py
from django.contrib import admin
from .models import Category, ModelItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

@admin.register(ModelItem)
class ModelItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'category']
    list_filter = ['category']
    search_fields = ['name']
