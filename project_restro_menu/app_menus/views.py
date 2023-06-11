from django.shortcuts import render
from app_menus.forms import CategoryCreateForm,MenuCreateForm

#Create your views here.
def list_menu(request):
    return render(request,'menus/list_menu.html')

def add_menu(request):
    menu_create_form = MenuCreateForm()#creating form class Object
    context = {"menu_create_form":menu_create_form,"title":"Create Menu here..."}
    return render(request,'menus/add_menu.html',context)
     

def edit_menu(request):
    return render(request,'menus/edit_menu.html')
def show_menu(request):
    return render(request,'menus/show_menu.html')  
