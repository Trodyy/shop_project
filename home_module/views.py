from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpRequest
from site_module.models import SiteSetting , FooterLink , Slider
from product_module.models import ProductCategory , Product , ProductVisit
from django.db.models import Count
# Create your views here.

class HomeView(TemplateView) :
   template_name = 'home_module/index.html'
   
   def get_context_data(self , **kwargs) :
       context = super().get_context_data(**kwargs)
       sliders = Slider.objects.all()
       context['sliders'] = sliders
       context['super_discount'] = Product.objects.get(is_main_discount=True)
       context["latest_products"] = Product.objects.filter(is_active=True).order_by('-id')[:6]
       most_visited = Product.objects.filter(is_active=True).annotate(visit_count=Count('pv')).order_by('-visit_count')[:12]
       context['most_visited'] = most_visited
       return context
       

def site_header_component(request : HttpRequest) :
    site_setting : SiteSetting = SiteSetting.objects.get(is_main_setting = True)
    categories = ProductCategory.objects.filter(is_active=True)
    context = {
        'site_setting' : site_setting ,
        'categories' : categories
    }
    return render(request , 'shared/site_header_components.html' , context)

def site_footer_component(request : HttpRequest) :
    site_setting : SiteSetting = SiteSetting.objects.get(is_main_setting = True)
    footer_links = FooterLink.objects.filter(is_active=True).all()
    context = {
        'site_setting' : site_setting ,
        'footer_links' : footer_links
    }
    return render(request , 'shared/site_footer_components.html' , context)