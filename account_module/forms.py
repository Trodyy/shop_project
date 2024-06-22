from django import forms

class RegisterForm(forms.Form) :
    email = forms.EmailField(
        label='ایمیل' ,
        widget=forms.EmailInput(attrs={
            'name' : 'email' ,
            'placeholder' : "Username@gmail.com"
            }) ,
        error_messages={
            'required' : 'لطفا ایمیل خود را وارد نمایید' ,
            'invalid' : 'ایمیل شما نامعتبر است'
        }
    )
    password = forms.CharField(
        label='رمز عبور' ,
        widget=forms.PasswordInput(attrs={
            'class' : 'pas' ,
            'name' : 'password'
            }) ,
        error_messages={
            'required' : 'لطفا رمز عبور خود را وارد نمایید' ,
            'invalid' : 'رمز عبور شما نامعتبر است'
        }
    )
    confirm_password = forms.CharField(
        label = 'تکرار رمز عبور' ,
        widget = forms.PasswordInput(attrs={
            'class' : 'pas' ,
            'name' : 'password'
            }) ,
        error_messages={
            'required' : 'لطفا تکرار رمز عبور خود را وارد نمایید' ,
            'invalid' : 'تکرار رمز عبور شما نامعتبر است'
        }
    )
    
    def check_password(self) :
        if self.password == self.confirm_password :
            return True
        else :
            return False
        
class LoginForm(forms.Form) :
    email = forms.EmailField(
        label='ایمیل' ,
        widget=forms.EmailInput(attrs={
            'name' : 'email' ,
            'placeholder' : "Username@gmail.com"
            }) ,
        error_messages={
            'required' : 'لطفا ایمیل خود را وارد نمایید' ,
            'invalid' : 'ایمیل شما نامعتبر است'
        }
    )
    password = forms.CharField(
        label='رمز عبور' ,
        widget=forms.PasswordInput(attrs={
            'class' : 'pas' ,
            'name' : 'password'
            }) ,
        error_messages={
            'required' : 'لطفا رمز عبور خود را وارد نمایید' ,
            'invalid' : 'رمز عبور شما نامعتبر است'
        }
    )   

class ForgotPasswordForm(forms.Form) :
    email = forms.EmailField(
        label='ایمیل' ,
        widget=forms.EmailInput(attrs={
            'name' : 'email' ,
            'placeholder' : "Username@gmail.com"
            }) ,
        error_messages={
            'required' : 'لطفا ایمیل خود را وارد نمایید' ,
            'invalid' : 'ایمیل شما نامعتبر است'
        }
    )
    
class ResetPasswordForm(forms.Form) :
    password = forms.CharField(
        label='رمز عبور' ,
        widget=forms.PasswordInput(attrs={
            'class' : 'pas' ,
            'name' : 'password'
            }) ,
        error_messages={
            'required' : 'لطفا رمز عبور خود را وارد نمایید' ,
            'invalid' : 'رمز عبور شما نامعتبر است'
        }
    )
    confirm_password = forms.CharField(
        label = 'تکرار رمز عبور' ,
        widget = forms.PasswordInput(attrs={
            'class' : 'pas' ,
            'name' : 'password'
            }) ,
        error_messages={
            'required' : 'لطفا تکرار رمز عبور خود را وارد نمایید' ,
            'invalid' : 'تکرار رمز عبور شما نامعتبر است'
        }
    )
    
    def check_password(self) :
        if self.password == self.confirm_password :
            return True
        else :
            return False
