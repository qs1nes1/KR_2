from django.shortcuts import render, get_object_or_404
from .models import Category, Recipe

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def main(request):
    recipes = Recipe.objects.filter(created_at__year=2024)
    return render(request, 'main.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})