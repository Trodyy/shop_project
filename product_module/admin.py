from django.contrib import admin
from . import models
# Register your models here.
class ProductAdmin(admin.ModelAdmin) :
    list_display = ('title' , 'price' , 'is_active')
    prepopulated_fields = {'slug' : ('title' , 'price')}
    
admin.site.register(models.Product , ProductAdmin)
admin.site.register(models.ProductCategory)
admin.site.register(models.ProductBrand)
admin.site.register(models.ProductVisit)