from django.contrib import admin
from django.db import models
from .models import Product,Tags,Category, Orderitem , Choice_test , Bookamrk , Order , Adrress_model

# Register your models here.

admin.site.register(Product)
admin.site.register(Tags)
admin.site.register(Category)
admin.site.register(Choice_test)
admin.site.register(Bookamrk)
admin.site.register(Adrress_model)



class OrderitemInline (admin.TabularInline) :
    model = Orderitem
    raw_id_fields = ('product',)

@admin.register(Order)
class Order_Admin (admin.ModelAdmin) :
    inlines =(OrderitemInline,)
