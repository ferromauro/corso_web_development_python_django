from django.db import models
from django.urls import reverse

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=180)
    description = models.TextField(max_length=800)
    ingredients = models.ManyToManyField('Ingredient')
    totalScore = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    calories = models.IntegerField(blank=False)
    type = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Order(models.Model):  
    name = models.CharField(max_length=20, blank=False)
    surname = models.CharField(max_length=20, blank=False)
    address = models.CharField(max_length=30, blank=False)
    street_number = models.IntegerField(blank=False)
    city = models.CharField(max_length=20, blank=False)
    email = models.EmailField(blank=False)
    info = models.TextField(blank=True)
    recipe = models.ForeignKey('Recipe', blank=False, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.recipe.name
    
    def get_absolute_url(self):
        return reverse('edit_order', kwargs={'pk': self.pk})
