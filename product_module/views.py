from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Product , ProductVisit , ProductSpecifications , ProductComment
from django.db.models import Count
from utils.client_ip import get_user_ip
from django.http import HttpRequest , HttpResponse
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
        
def product_comment(request : HttpRequest , product) :
    comments = ProductComment.objects.filter(product_id = product.id , is_active = True , parent_id = None).prefetch_related('productcomment_set').order_by('-id')
    context = {
        'comments' : comments ,
        'comment_count' : ProductComment.objects.filter(is_active = True , product_id = product.id).count()
    }
    return render(request , 'product_module/components/comments.html' , context)

def add_product_comment(request : HttpRequest) :
    if request.user.is_authenticated :
        comment_text = request.GET.get('comment')
        product_id = request.GET.get('product_id')
        parent_id = request.GET.get('parent_id')
        new_comment = ProductComment(parent_id = parent_id if parent_id is not '' else None , product_id = product_id , user_id = request.user.id , text = comment_text , is_active = True)
        new_comment.save()
        comments = ProductComment.objects.filter(product_id = product_id , is_active = True , parent_id = None).prefetch_related('productcomment_set').order_by('-id')
        context = {
        'comments' : comments ,
        'comment_count' : ProductComment.objects.filter(is_active = True , product_id = product_id).count()
    }
        return render(request , 'product_module/components/comments.html' , context)
    return HttpResponse('i hpe that i will be successfull')
    