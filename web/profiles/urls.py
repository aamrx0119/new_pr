from django.urls import path
from . import views

app_name = 'profiles'
urlpatterns = [
    path('',views.Profile_dashboard,name='profile_dashboard_view'),
]
