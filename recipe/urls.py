from django.urls import path
from . import views

urlpatterns = [
    path('2023/', views.main, name='main'),
    path('<int:id>/', views.recipe_detail, name='recipe_detail'),
]
