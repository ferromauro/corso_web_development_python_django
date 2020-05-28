from django import forms
from recipe.models import Order

CHOICES=[("1","1 Stella"),("2","2 Stelle"),("3","3 Stelle"),("4","4 Stelle"),("5","5 Stelle")]

class voteForm(forms.Form):
    rating = forms.ChoiceField(choices=CHOICES)


class orderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['recipe', 'name', 'surname', 'address', 'street_number', 'city', 'email', 'info']
