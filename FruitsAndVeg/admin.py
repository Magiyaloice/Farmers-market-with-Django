from django.contrib import admin 
from . models import FruitsAndVeg

class FruitsAndVegAdmin(admin.ModelAdmin):
    list_display = ('name','price','quantity')

admin.site.register(FruitsAndVeg, FruitsAndVegAdmin)
