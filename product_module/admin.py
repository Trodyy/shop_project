from typing import Any
from django.contrib import admin
from . import models
# Register your models here.
class ProductAdmin(admin.ModelAdmin) :
    list_display = ('title' , 'price' , 'is_active')
    prepopulated_fields = {'slug' : ('title' , 'price')}

class ProductCommentAdmin(admin.ModelAdmin) :
    def save_model(self, request: Any, obj: models.ProductComment, form, change) :
        if not change :
            obj.user = request.user
        return super().save_model(request, obj, form, change)

admin.site.register(models.Product , ProductAdmin)
admin.site.register(models.ProductCategory)
admin.site.register(models.ProductBrand)
admin.site.register(models.ProductVisit)
admin.site.register(models.ProductSpecifications)
admin.site.register(models.ProductComment , ProductCommentAdmin)