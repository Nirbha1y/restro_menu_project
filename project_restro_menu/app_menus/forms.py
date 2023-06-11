from django import forms
from app_menus.models import Category,Menu

class CategoryCreateForm(forms.ModelForm):
    class Meta:
      #  fields =("__all__",)#for all attributes
        fields = ("category_title","category_code")
        model = Category

class MenuCreateForm(forms.ModelForm):
    class Meta:
        fields = ("menu_title","menu_price","menu_ingredient","menu_category")
        model = Menu

