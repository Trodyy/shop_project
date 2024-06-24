from django.db import models

# Create your models here.
class SiteSetting(models.Model) :
    title = models.CharField(max_length=50 , verbose_name = 'عنوان')
    logo = models.ImageField(upload_to='images/site-logo/' , verbose_name='لوگو')
    copy_right = models.CharField(max_length=500 , verbose_name='متن کپی رایت')
    address = models.CharField(max_length=300 , verbose_name='آدرس')
    call_number = models.IntegerField(verbose_name='شماره تماس')
    fax =  models.IntegerField(verbose_name='فکس')
    is_main_setting = models.BooleanField(verbose_name='تنظیمات اصلی ؟')
    about_us = models.TextField(verbose_name='درباره ما')
    
    class Meta :
        verbose_name = 'تنظیم سایت'
        verbose_name_plural = 'تنظیمات سایت'
        
    def __str__(self) :
        return self.title
    
class FooterLink(models.Model) :
    title = models.CharField(max_length = 100 , verbose_name = 'عنوان')
    url_title = models.CharField(max_length=100 , verbose_name='عنوان درurl')
    is_active = models.BooleanField(verbose_name = 'فعال / غیرفعال')
    link = models.URLField(max_length=300)
    
    class Meta :
        verbose_name = 'لینک فوتر'
        verbose_name_plural = 'لینک های فوتر'
        
    def __str__(self) :
        return f'{self.title} / {self.url_title}'
    
class Slider(models.Model) :
    image = models.ImageField(upload_to = 'image/slider/' , verbose_name = 'تصویر')
    title = models.CharField(max_length=70 , verbose_name='عنوان')
    text = models.TextField(verbose_name='متن')
    url = models.URLField(max_length=200 , verbose_name='URL')
    
    class Meta :
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدرها'
        
    def __str__(self) :
        return self.title
    