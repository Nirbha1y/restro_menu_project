from django.urls import path
from app_menus import views 
urlpatterns =[
    path('', views.list_menu , name='menu-list'),
    path('add/', views.add_menu, name='menu-add'),
    path('edit/<int:id>/', views.edit_menu , name='menu-edit'),
    path('show/<int:id>/', views.show_menu, name='menu-show'),
    path('delete/<int:id>/',views.delete_menu, name="menu-delete")


]