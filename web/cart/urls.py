from django.urls import path
from . import views

app_name = 'cart'


urlpatterns = [
    path('',views.shop_summary,name='checkout_summary_view'),
    path('<slug:slug>/',views.checkout_add,name='add'),
    path('<slug:slug>/delete/',views.checkout_delete,name='delete'),
]
