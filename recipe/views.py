# views.py
from django.shortcuts import render, get_object_or_404
from .models import Recipe

def main(request):
    recipes_2023 = Recipe.objects.filter(created_at__year=2023)
    return render(request, 'main.html', {'recipes': recipes_2023})

def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})
