# urls.py
from django.urls import path
from .views import main, recipe_detail

urlpatterns = [
    path('', main, name='main'),
    path('recipe/<int:id>/', recipe_detail, name='recipe_detail'),
]
