from django.urls import path
from app_menus import views 
urlpatterns =[
    path('', views.list_menu , name='menu-list'),
    path('add/', views.add_menu, name='menu-add'),
   # path('edit/', views.edit_menu , name='menu-edit'),
   # path('show/', views.show_menu, name='menu-show')

]