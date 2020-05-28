from django.shortcuts import render, redirect
from recipe.models import Recipe, Ingredient
from django.http import Http404, HttpResponseServerError
from recipe.forms import voteForm
from recipe.forms import orderForm
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView

from recipe.models import Order, Recipe

from django.urls.base import reverse_lazy

# Create your views here.
def home(request):
    recipes = Recipe.objects.all()
    context = {'recipes':recipes}
 #   return render(request, 'home_old.html', context)
    return render(request, 'home.html', context)

def recipe_detail(request, recipe_id):
    if request.method == 'POST':
        form = voteForm(request.POST)
        if form.is_valid():
            try:
                recipe = Recipe.objects.get(id=recipe_id)
                recipe.votes += 1
                recipe.totalScore += int(form.cleaned_data['rating'])
                recipe.save()
            except Recipe.DoesNotExist:
                raise Http404('Recipe not found.')    
    
    try:
        recipe = Recipe.objects.get(id=recipe_id)
        calories = 0
        form = voteForm()
        
        if recipe.votes !=0:
            rating = round(recipe.totalScore/recipe.votes,1)
        else:
            rating = 0

        if recipe.ingredients.all():
            for i in recipe.ingredients.all():
                calories += i.calories
            calories = calories//len(recipe.ingredients.all())
        else:
            calories = 0       
        context = {
            'recipe':recipe, 
            'calories': calories, 
            'form':form,
            'rating':rating,
            }
    except Exception as e:
        print(e)
        raise Http404()
    return render(request, 'recipe_detail.html', context) 

def error_404(request,exception):
    return render(request, '404.html', status=404 )

def order_new(request):
    if request.method == 'POST':
        form = orderForm(request.POST)
        if form.is_valid():
            try:
                order = form.save()
            except: 
                raise HttpResponseServerError()
            return redirect('order_list')
        else: 
            note = 'Error on validation order, please submit a new order.'
            context = {'form':form,'note':note}               
            return render(request, 'order_new.html', context) 
    else:
        form = orderForm
        context = {'form':form, 'note':''}
        return render(request, 'order_new.html', context)




class order_all(ListView):
    model = Order


class edit_order(UpdateView):
    model = Order
    form_class = orderForm
    template_name_suffix= '_update_page'
    
class remove_order(DeleteView):
    model = Order
    success_url = reverse_lazy('order_list')




