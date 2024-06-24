from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.shortcuts import reverse 
from account_module.models import User
# Create your models here.
class ProductCategory(models.Model) :
    title = models.CharField(max_length=50 , verbose_name = 'عنوان')
    url_title = models.CharField(max_length=100 , verbose_name = 'عنوان در url')
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال')
    
    class Meta :
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        
    def __str__(self) :
        return self.title

class ProductBrand(models.Model) :
    title = models.CharField(max_length=50 , verbose_name = 'عنوان')
    url_title = models.CharField(max_length=100 , verbose_name = 'عنوان در url')
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال')
    
    class Meta :
        verbose_name = 'برند'
        verbose_name_plural = 'برند ها'
        
    def __str__(self) :
        return self.title
    
class Product(models.Model) :
    title = models.CharField(max_length=50 , verbose_name = 'عنوان')
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال')
    price = models.IntegerField(verbose_name='قیمت' , default=0 , validators=[MinValueValidator(0)])
    slug = models.SlugField(default="", null=False, db_index=True, blank=True, max_length=200, unique=True,
                            verbose_name='عنوان در url')
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال')
    brand = models.ForeignKey('ProductBrand' , on_delete=models.CASCADE , verbose_name='برند' , related_name='brands')
    category = models.ForeignKey('ProductCategory' , on_delete=models.CASCADE , verbose_name='دسته بندی' , related_name='categories' , default='')
    is_main_discount = models.BooleanField(verbose_name='تخفیف ویژه ؟' , default=False)
    description = models.TextField(verbose_name = 'توضیحات' , null=True)
    image = models.ImageField(upload_to='products' , null=True , blank=True , verbose_name=' تصویر')
    
    class Meta :
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
        
    def __str__(self) :
        return f'{self.title} / {self.price}'
    
    def get_absolute_url(self) :
        return reverse('product_detail' , args=[self.slug] )

class ProductVisit(models.Model) :
    product = models.ForeignKey('Product' , on_delete = models.CASCADE , verbose_name = 'نام محصول' , related_name='pv')
    ip = models.CharField(max_length = 30 , verbose_name = 'آی پی کاربر')
    user = models.ForeignKey(User , null = True , blank = True , verbose_name = 'کاربری که مشاهده کرده' , on_delete = models.CASCADE)


    def __str__(self) :
        return f'{self.product.title}  /{self.ip}'
    
    class Meta :
        verbose_name  ='بازدید محصول'
        verbose_name_plural = 'بازدید محصولات'
    