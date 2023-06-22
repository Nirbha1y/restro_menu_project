from django.contrib import admin
from app_menus.models import Category,Menu
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["category_title","category_code"]
    search_fields = ["category_title","category_code"]
    list_filter = ["category_title",] 

class MenuAdmin(admin.ModelAdmin):
   list_display = ("menu_title","menu_category","menu_price","menu_ingredient","menu_created_at")
   search_fields = ("menu_title",)
   list_filter = ("menu_title","menu_category")


admin.site.register(Category, CategoryAdmin)
admin.site.register(Menu,MenuAdmin)

#customizing admin panel title and headings
admin.site.site_title="Admin Panel" #page sub title
admin.site.site_header="RESTRO" #page header
admin.site.index_title="RESTRO" #page title