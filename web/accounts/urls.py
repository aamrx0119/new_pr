from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('reset/', views.Userresetpassword.as_view(),name='reset_password'),
    path('reset/done/', views.PasswordResetDone.as_view(),name='password_reset_done'),
    path('confirm/reset/<uidb64>/<token>/', views.password_reset_confirm.as_view(),name='password_reset_confirm'),
    path('confirm/done/', views.password_reset_complete.as_view(),name='password_reset_complete'),
    path('login/',views.Login_account,name='accounts_login_view'),
    path('signup/',views.Signup_account,name='accounts_signup_view'),
    path('logout/',views.Logout_account,name='accounts_logout_view'),
    # path('acc/google/',views.Logout_account,name='accounts_logout_view'),

]
