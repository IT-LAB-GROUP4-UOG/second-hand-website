from django import forms
from .models import Item, ItemImage


class ItemForm(forms.ModelForm):
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}),
                              required=False)

    class Meta:
        model = Item
        fields = ['title', 'description', 'price', ]
