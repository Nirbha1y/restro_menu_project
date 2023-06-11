from django.db import models

# Create your models here.
class Category(models.Model):
    category_title= models.CharField(max_length=100)
    category_code = models.CharField(max_length=20,null=True,blank=True)

    class Meta:
       db_table = "restro_categories"
       ordering = ["-category_title"] 

class Menu(models.Model):
    menu_title = models.CharField(max_length=100)
    menu_price = models.FloatField(default=0.00)
    menu_ingredient = models.CharField(max_length=100)
    menu_category = models.ForeignKey(Category,on_delete=models.CASCADE)
    menu_img = models.FileField(upload_to="images/menus/", blank=True ,null =True)
    menu_created_at =  models.DateTimeField(auto_now_add=True)    
    is_active =models.BooleanField(default=True)



    class Meta:
        db_table = "restro_menus"
        ordering = ["-menu_title"]

       




#metadata= data ko data        