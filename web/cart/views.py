
from django.shortcuts import redirect, render
from home.models import Product
from .cartttt import Cart
from home.forms import Order_Item_form
from home.forms import quantity_form
# Create your views here.




def shop_summary(reuqest):
    cart = Cart(reuqest)
    return render (reuqest,'cart/checkout.html',{'cart':cart,})



def checkout_add (request,slug) :
    cart = Cart(request)
    if request.method == 'POST' :
        product = Product.objects.get(slug=slug)
        form = quantity_form(request.POST)
        if form.is_valid () :
            cd = form.cleaned_data
            cart.add(product=product,quantity=cd['quantity1'])
    return redirect('cart:checkout_summary_view')

def checkout_delete (request,slug) :
    cart = Cart(request)
    product = Product.objects.get(slug=slug)
    cart.Delete_session(product=product)
    return redirect('cart:checkout_summary_view')
