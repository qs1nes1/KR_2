from django.contrib import admin
from django.urls import path
from recipe import views

app_name = 'recipe'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories/', views.category_list, name='category_list'),
    path('', views.main, name='main'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
]