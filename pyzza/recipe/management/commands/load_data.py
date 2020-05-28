from django.core.management import BaseCommand
from recipe.models import Ingredient

class Command(BaseCommand):
    help = "Load data from alimenti.txt into DB"
    def handle(self,*args,**options):
        print("Loading data from file ingredienti.CSV")
        f = open('./ingredienti.CSV')
        for row in f:
            row = row.replace('\n','')
            dataline = row.split(';')
            new_ingredient = Ingredient()
            new_ingredient.name = dataline[0]
            new_ingredient.calories = dataline[1]
            new_ingredient.type = dataline[2]
            new_ingredient.save()
