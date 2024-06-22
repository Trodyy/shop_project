from django.shortcuts import render , reverse , redirect
from .models import User
from .forms import RegisterForm , LoginForm , ForgotPasswordForm , ResetPasswordForm
from django.views import View
from django.http import HttpRequest
from django.utils.crypto import get_random_string
from utils.email_service import send_email
from django.contrib.auth import logout , login

# Create your views here.

class RegisterView(View) :
    def get(self, request):
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }

        return render(request, 'account_module/register.html', context)
    
    def post(self , request : HttpRequest) :
        register_from = RegisterForm(request.POST)
        if register_from.is_valid() :
            user_email = register_from.cleaned_data.get('email')
            print(register_from.check_password)
            if register_from.check_password :
                user_password = register_from.cleaned_data.get('password')
                user : bool = User.objects.filter(email = user_email).exists()
                if not user :
                    new_user : User = User(username=user_email , email = user_email , email_active_code=get_random_string(72) , is_active=False)
                    new_user.set_password(user_password)
                    new_user.save()
                    send_email('فعالسازی حساب کاربری' , user_email , {'user' : new_user} , 'emails/active_email.html')
                    return redirect(reverse('login_page'))
                else :
                    register_from.add_error('email' , 'ایمیل شما قبلا ثبت نام شده است')
            else :
                register_from.add_error('password' , 'رمز عبور و تکرار رمز عبور بایستی  یکسان باشند')  
        else :
            register_from.add_error('email' , 'لطفا اطلاعات خود را به درستی وارد کنید')
        context = {
            'register_from' : register_from
        }
        return render(request , 'account_module/register.html' , context)
    
class ActivateAccount(View) :
    def get(request : HttpRequest , self , active_code) :
        user : User = User.objects.filter(email_active_code__iexact = active_code).first()
        if user is not None :
            user.is_active = True
            user.email_active_code = get_random_string(72)
            user.save()
            return redirect(reverse('login_page'))
    
class LoginView(View) :
    def get(self , request : HttpRequest) :
        login_form = LoginForm()
        context = {
            'login_form' : login_form
        }
        return render(request , 'account_module/login.html' , context)
    
    def post(self , request : HttpRequest) :
        login_form = LoginForm(request.POST)
        if login_form.is_valid() :
            user_email = login_form.cleaned_data.get('email')
            user_password = login_form.cleaned_data.get('password')
            user : User = User.objects.filter(email = user_email).first()
            if user.is_active :
                if user is not None :
                    checking_user = user.check_password(user_password)
                    if checking_user :
                        login(request , user)
                        return redirect(reverse('index_page'))
                    else :
                        login_form.add_error('password' , 'رمز عبور شما اشتباه است')
                else :
                    login_form.add_error('email' , 'لطفا ابتدا ثبت نام کنید')
            else :
                login_form.add_error('email' , 'لطفا ابتدا حساب کاربری خود را فعال کنید' )
        context = {
             'login_form' : login_form
        }
        return render(request , 'account_module/login.html' , context)
    
class ForgotPasswordView(View) :
    def get(self , request : HttpRequest) :
        forgot_password_form = ForgotPasswordForm()
        context = {
            'forgot_password_form' : forgot_password_form
        }
        return render(request , 'account_module/forgot_password.html' , context)
    
    def post(self , request : HttpRequest) :
        forgot_password_form = ForgotPasswordForm(request.POST)
        if forgot_password_form.is_valid() :
            user_email = forgot_password_form.cleaned_data.get('email')
            user : User = User.objects.filter(email__iexact = user_email).first()
            if user is not None :
                if user.is_active :
                    send_email('فراموشی رمز عبور' , user_email , {'user' : user} , 'emails/forgot_password.html')
                    return redirect(reverse('reset_password' , args=[user.email_active_code]))
                else :
                    forgot_password_form.add_error('email' , 'ابتدا حساب کاربری خود را فعال کنید')
            else :
                forgot_password_form.add_error('email' , 'لطفا ابتدا ثبت نام کنید')
        context = {
            'forgot_password_form' : forgot_password_form
        }
        return rnder(request , 'account_module/forgot_password.html' , context)
    
class ResetPasswordView(View) :
    def get(self , request : HttpRequest , reset_code) :
        reset_password_form = ResetPasswordForm()
        context = {
            'reset_password_form' : reset_password_form
        }
        return render(request , 'account_module/reset_password.html' , context)
    
    def post(self , request : HttpRequest , reset_code) :
        reset_password_form = ResetPasswordForm(request.POST)
        if reset_password_form.is_valid() :
            user_password = reset_password_form.cleaned_data.get('password')
            user : User = User.objects.filter(email_active_code__iexact = reset_code).first()
            if user is not None :
                if reset_password_form.check_password() :
                    user.set_password(user_password)
                    user.save()
                    redirect(reverse('login_page'))
                else :
                    reset_password_form.add_error('confirm_password' , 'رمز عبور و تکرار رمز عبور بایتسی یکسان باشند')
            else :
                reset_password_form.add_error('password' , 'لطفا ابتدا ثبت نام کنید')
        else :
            reset_password_form.add_error('password' , 'لطفا مقادیر معتبر را وارد نمایید')
        context = {
            'reset_password_form' : reset_password_form
        }
        return render(request , 'account_module/reset_password.html' , context)

class LogOutView(View) :
    def get(self , request : HttpRequest) :
        logout(request)
        return redirect(reverse('index_page'))