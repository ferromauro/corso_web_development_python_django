from django.contrib import admin
from recipe.models import Recipe, Ingredient, Order
# Register your models here.

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    pass

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display=['name','type', 'calories']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['id','recipe','name','surname', 'email']