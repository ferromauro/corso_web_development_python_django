from django.test import TestCase
from recipe.models import Recipe, Ingredient, Order
from model_bakery import baker

from django.urls import reverse

class ModelTestcase(TestCase):
    def setUp(self):
        self.recipe = baker.make(Recipe)
        self.ingredient = baker.make(Ingredient)
        self.order = baker.make(Order)
    
    def test_recipe_str(self):
        self.assertEqual(self.recipe.__str__(), self.recipe.name)

    def test_ingredient_str(self):
        self.assertEqual(self.ingredient.__str__(), self.ingredient.name)

    def test_order_str(self):
        self.assertEqual(self.order.__str__(), self.order.recipe.name)

    def test_get_absolute_url(self):
        url = reverse('edit_order', kwargs={'pk':self.order.pk})
        self.assertEqual(url,self.order.get_absolute_url())