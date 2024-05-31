from django.test import TestCase, Client
from django.urls import reverse
from .models import Recipe
from datetime import datetime

class RecipeViewsTestCase(TestCase):
    def setUp(self):
        # Створення тестових даних для рецептів
        self.recipe1 = Recipe.objects.create(
            title='Перший рецепт',
            created_at=datetime(2023, 1, 1),
            description='Опис першого рецепту'
        )
        self.recipe2 = Recipe.objects.create(
            title='Другий рецепт',
            created_at=datetime(2022, 1, 1),
            description='Опис другого рецепту'
        )

    def test_main_view(self):
        client = Client()
        response = client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        self.assertContains(response, 'Перший рецепт')
        self.assertNotContains(response, 'Другий рецепт')

    def test_recipe_detail_view(self):
        client = Client()
        response = client.get(reverse('recipe_detail', kwargs={'id': self.recipe1.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe_detail.html')
        self.assertContains(response, 'Опис першого рецепту')
