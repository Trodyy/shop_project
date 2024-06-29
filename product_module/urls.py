from django.urls import path
from . import views

urlpatterns = [
    path('' , views.ProductListView.as_view() , name = 'product_list') ,
    path('details/<slug:slug>/' , views.ProductDetailView.as_view() , name = 'product_detail') ,
    path('category/<cat>/' , views.ProductListView.as_view() , name = 'selected_category') ,
    path('add-product-comment/' , views.add_product_comment , name = 'add_product_comment') ,
]