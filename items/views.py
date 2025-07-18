from django.shortcuts import render, get_object_or_404
from .models import Category, ModelItem

def home(request):
    categories = Category.objects.all()  # ✅ For homepage categories
    return render(request, 'items/home.html', {'categories': categories})

def model_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    models = ModelItem.objects.filter(category=category)
    categories = Category.objects.all()  # ✅ All categories always shown
    return render(request, 'items/model_list.html', {
        'category': category,
        'models': models,
        'categories': categories
    })

def index(request):
    return render(request, 'items/index.html')
