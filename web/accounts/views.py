from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .forms import user_login_form , user_signup_form ,EmailValidationOnForgotPassword , Changeeee
from .models import MyUser
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy



# Create your views here.
def Login_account (request) :
    pm = False
    if request.method == 'POST' :
        form = user_login_form(request.POST)
        if form.is_valid() :
            cd = form.cleaned_data
            user = authenticate(email = cd['email'],password = cd['password'])
            if user is not None :
                login(request,user)
                pm = True
                messages.success(request,'You login successfuly','success')
                return redirect ("home:home_page_view")
            else:
                messages.error(request,'email or password is wrong','danger')              
    form= user_login_form()
    return render (request,'accounts/login_page.html',{'form':form,'pm':pm,})


def Signup_account (request) :
    pm = False
    if request.method == 'POST' :
        form = user_signup_form(request.POST)
        if form.is_valid() :
            cd = form.cleaned_data
            user=MyUser.objects.create_user(email=cd['email'],last_name=cd['last_name'],first_name=cd['first_name'],password=cd['password'],bio=None)
            user.save()
            messages.success(request,'You sign up successfuly','success')
            return redirect ("accounts:accounts_login_view")
            pm = True   
    form= user_signup_form()
    return render (request,'accounts/signup_page.html',{'form':form,'pm':pm,})


def Logout_account (request) :
    logout(request)
    return redirect('home:home_page_view')







class Userresetpassword(auth_views.PasswordResetView):
    template_name = 'accounts/resetpass/password_reset_form.html'
    success_url =  reverse_lazy ('accounts:password_reset_done')
    html_email_template_name = 'accounts/resetpass/password_reset_email.html'
    form_class=EmailValidationOnForgotPassword


class PasswordResetDone (auth_views.PasswordResetDoneView):
    template_name = 'accounts/resetpass/reset_done.html'


class password_reset_confirm(auth_views.PasswordResetConfirmView):
    template_name = 'accounts/resetpass/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')
    form_class = Changeeee

class password_reset_complete(auth_views.PasswordResetCompleteView):
    template_name = 'accounts/resetpass/password_reset_complete.html'



#<<<<<  URL >>>>>>>
# app_name = 'accounts'
# urlpatterns = [
#     path('reset/', views.Userresetpassword.as_view(),name='reset_password'),
#     path('reset/done/', views.PasswordResetDone.as_view(),name='password_reset_done'),
#     path('confirm/reset/<uidb64>/<token>/', views.password_reset_confirm.as_view(),name='password_reset_confirm'),
#     path('confirm/done/', views.password_reset_complete.as_view(),name='password_reset_complete'),
# ]



