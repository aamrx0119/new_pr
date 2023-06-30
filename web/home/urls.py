from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('',views.Home_Page,name='home_page_view'),
    path('get_new/',views.Get_New_Products,name='get_new'),
    path('detail/<slug:slug>/',views.Product_Detail_Page,name='detail_page_view'),
    path('bookmark/',views.Bookmark,name='bookmark_view'),
    path('add_order/',views.Add_Order,name='add_order_view'),
    path('f/<int:order_id>/',views.Finall_Check,name='finall_check'),
    path('search/',views.search_results,name='search'),
    path('cat/<slug:cat>/',views.filter_views,name='fiter_view'),
]
