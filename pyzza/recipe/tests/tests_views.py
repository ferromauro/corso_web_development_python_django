from django.test import TestCase
from django.test import Client
from django.urls import reverse
from model_bakery import baker
from recipe.models import Recipe
from recipe.forms import orderForm

class ViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.recipe = baker.make(Recipe, make_m2m=True)
        self.recipe.save()
  
    def test_recipe_detail(self):
        url = reverse('recipe_detail', kwargs={'recipe_id':self.recipe.id})
        page = self.client.get(url)
        self.assertEqual(page.status_code, 200)
