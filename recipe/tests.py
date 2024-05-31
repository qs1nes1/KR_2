from django.test import TestCase
from django.urls import reverse
from .models import Category, Recipe


class RecipeViewsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(name='Test Category')
        cls.recipe = Recipe.objects.create(
            title='Test Recipe',
            description='Test Description',
            instructions='Test Instructions',
            ingredients='Test Ingredients',
            category=cls.category
        )

    def test_category_list_view(self):
        response = self.client.get(reverse('category_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category_list.html')
        categories = Category.objects.all()
        self.assertQuerysetEqual(response.context['categories'], categories)


    def test_main_view_with_recipes(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        recipes = Recipe.objects.filter(created_at__year=2024)
        self.assertQuerysetEqual(response.context['recipes'], recipes)

    def test_main_view_no_recipes(self):
        Recipe.objects.all().delete()
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        self.assertContains(response, 'No recipes found.')

    def test_recipe_detail_view(self):
        response = self.client.get(reverse('recipe_detail', args=[self.recipe.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe_detail.html')
        self.assertContains(response, self.recipe.title)