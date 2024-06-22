from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser) :
    avatar = models.ImageField(upload_to = 'images/avatars/' , verbose_name = 'آواتار کاربر')
    email_active_code = models.CharField(max_length=300 , null=True , blank=True , verbose_name='کد فعالسازی')
    address = models.CharField(max_length=300 , verbose_name = 'آدرس')
    
    def __str__(self) :
        if self.first_name != '' and self.last_name != '' :
            return self.get_full_name()
        else :
            return self.email
    
    class Meta :
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
        