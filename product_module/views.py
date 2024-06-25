from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Product , ProductVisit , ProductSpecifications
from django.db.models import Count
from utils.client_ip import get_user_ip
# Create your views here.
class ProductListView(ListView) :
    template_name = 'product_module/product_list.html'
    model = Product
    context_object_name = 'products'
    
    def get_context_data(self , **kwargs) :
        context = super().get_context_data(**kwargs)
        return context
    
    def get_queryset(self) :
        query = super(ProductListView, self).get_queryset()
        category = self.kwargs.get('cat')
        if category is not None :
            query = query.filter(category__url_title__iexact =category)
        return query
            

class ProductDetailView(DetailView) :
    model = Product
    template_name  ='product_module/product_detail.html'
    context_object_name = 'product'
    
    def get_context_data(self,**kwargs) :
        context = super().get_context_data(**kwargs)
        loaded_product = self.object
        new_visit = ProductVisit(product=self.object , ip=get_user_ip(self.request) , user=self.request.user)
        new_visit.save()
        context['Specifications'] = ProductSpecifications.objects.filter(product_id = loaded_product.id)
        context['revelants'] = Product.objects.filter(category__url_title__iexact = loaded_product.category.url_title).exclude(id = loaded_product.id)
        return context
        
        