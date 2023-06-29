from django.shortcuts import render, redirect
from app_menus.forms import CategoryCreateForm,MenuCreateForm
from app_menus.models import Menu, Category
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


#Create your views here.
@login_required(login_url = '/login/')
def list_menu(request):
    menu_list =Menu.objects.all()
    paginator = Paginator(menu_list, 4 ) # 4 data in one page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {  "page_obj" : page_obj }
    return render(request,'menus/list_menu.html',context)

@login_required(login_url = '/login/')
def show_menu(request,id):
    menu_obj = Menu.objects.get(id =id)
    context = {"data":menu_obj}
  
    return render(request, 'menus/show_menu.html',context)

@login_required(login_url = '/login/')
def edit_menu(request,id):
    menu_obj = Menu.objects.get(id =id)
    category_obj= Category.objects.all()
    context ={"data":menu_obj ,"categories": category_obj}
    context = {"data":menu_obj}

    if request.method =="POST":
        #to update data

        menu_obj = MenuCreateForm(data=request.POST, instance =menu_obj)
        if menu_obj.is_valid():
            menu_obj.save()
            return redirect("menu_edit") #redirecting to url having id


    return render(request, 'menus/edit_menu.html',context)

@login_required(login_url = '/login/')
def delete_menu(request,id):
    menu_obj =Menu.objects.get(id =id)
    menu_obj.delete()
    return redirect('menu-list')
    
    return redirect('menu-list')

@login_required(login_url = '/login/')
def add_menu(request):
    menu_create_form = MenuCreateForm()#creating form class Object
    context = {"menu_create_form":menu_create_form,"title":"Create Menu here..."}

    if request.method == "POST":
        menu_title = request.POST.get('menu_title') 
        menu_price = request.POST.get('menu_price')
        menu_ingredient = request.POST.get('menu_ingredient')
        # menu_category = request.POST.get('menu_category')
        category_obj = Category.objects.get(id=request.POST.get('menu_category'))
        #method 1
       #
        menu =MenuCreateForm(request.POST)
        if menu.is_valid():
            menu.menu_category = category_obj
            menu.save()
            return redirect("menu-list")
        return redirect("menu-add")  
    return render(request,'menus/add_menu.html',context)
     

      #method 2
      #menu =Menu(menu_title=menu_title, menu_price=menu_price, menu_category=category_obj, menu_ingredient=menu_ingredient)
      #menu_obj.save()
         
#method one
        # menu_obj = Menu()
        # menu_obj.menu_title = menu_title
        # menu_obj.menu_price = menu_price
        # menu_obj.menu_category = category_obj # passing Category Object (Foreign Key Object)
        # menu_ingredient = menu_ingredient
        # menu_obj.save()
        # # method two
        # menu = Menu(menu_title=menu_title, menu_price=menu_price,
        #             menu_category=category_obj, menu_ingredient=menu_ingredient)
        # menu.save()

        # method three - storing data with Form Class Object
    #     menu = MenuCreateForm(request.POST)
    #     if menu.is_valid():
    #         menu.menu_category = category_obj
    #         menu.save()
    #         return redirect("menu-list")
    #     return redirect("menu-add")
    # return render(request, 'menus/add_menu.html', context)
      #method 3: storing data eith form class objects
      