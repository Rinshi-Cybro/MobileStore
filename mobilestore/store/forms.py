from django import forms
from account.models import User
from .models import ProductModel

class ProductForm(forms.ModelForm):
    class Meta:
        model=ProductModel
        fields="__all__"


class StoreForm(forms.ModelForm):
    class Meta:
        model=User
        fields="__all__"        