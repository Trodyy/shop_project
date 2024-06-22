from django.urls import path
from . import views

urlpatterns = [
    path('register/' , views.RegisterView.as_view() , name = 'register_page') ,
    path('login/' , views.LoginView.as_view() , name = 'login_page') ,
    path('activate-account/<active_code>/' , views.ActivateAccount.as_view() , name = 'activate_account') ,
    path('forgot-password/' , views.ForgotPasswordView.as_view() , name = 'forgot_password') ,
    path('reset-password/<reset_code>/' , views.ResetPasswordView.as_view() , name = 'reset_password') ,
    path('logout/' , views.LogOutView.as_view() , name = 'logout_page') ,
]