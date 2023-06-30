
from itertools import product
from django import forms
from django.shortcuts import redirect, render
from django.db.models import Q
from .models import Order, Product , Category , Tags,Orderitem , Bookamrk  ,Adrress_model
from .forms import Order_Item_form,quantity_form , Choice_test_form , Adrress_form ,Get_Products
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random
from cart.cartttt import Cart
from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup
from .web_SC import Web_Scraping , Adidas
# Create your views here.


def Home_Page (request) :
    search_bar=Product.objects.all()
    category = Category.objects.filter(sub=False)

    posts = Product.objects.all()[:6]

    page = request.GET.get('page', 1)

    paginator = Paginator(posts, 2)
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)

    if request.method == 'POST' :
        form =Choice_test_form(request.POST)
        if form.is_valid() :
            form.save()
    form = Choice_test_form()



    context = {
        'post':post,
        'form':form,
        'posts':posts,
        'search_bar':search_bar,
        'category':category,
    
    

    }
    return render(request,'home/home_page.html',context)


def Get_New_Products(request):
    Catt=Category.objects.get(title='man')
    taggsss= Tags.objects.all()
    if request.method == 'POST':
        form = Get_Products(request.POST)
        if form.is_valid():
            # brand= request.POST.get('Title')
            cd = form.cleaned_data 
            if cd['Title'] == 'Nike':
                product = Web_Scraping(cd['Title'],cd['sex'],cd['product'],cd['quantity'])
                product.Nike(Catt,taggsss)
            else:
                product = Adidas(cd['Title'],cd['sex'],cd['product'],cd['quantity'])
                product.Adidas_clothes(Catt,taggsss)

    form=Get_Products()

    context={
        'form':form,
    }


    return render(request,'home/get_new_products.html',context)





def search_results (request) :
    if request.is_ajax() :
        res = None
        product = request.POST.get('product')
        qs = Product.objects.filter(name__icontains=product)
        if len(qs) > 0 and len(product) > 0 :
            data = []
            for pos in qs :
                item = {
                    'pk' : pos.pk,
                    'name' : pos.name,
                    'image' : str(pos.image.url),
                    'slug' : str(pos.slug)
                }
                data.append(item)
            res = data
        else:
            res = 'No product found ...'
    
        return JsonResponse({'data':res})
    return JsonResponse({})


def random_color () :
    list_item =['primary','danger','warning']
    for x in  range(0,4) :
        for r in random.choices(list_item):
            return r


def Product_Detail_Page (request,slug) :
    req = requests.get('https://www.tgju.org/profile/price_try')
    result = BeautifulSoup(req.text,'html.parser')
    r=result.find('span',{'data-col':'info.last_trade.PDrCotVal'})
    price = str((r.text))
    x=price.replace(',','')
    n=(int(x))
    
    user = request.user
    product = Product.objects.get(slug = slug)
    stats = False
    book = Bookamrk.objects.filter(user=user,product=product,status='yes')
    if book.exists():
        stats=True

    for i in range (0,2) :       
        list_item =['primary','danger','warning']
        bigh= random.choice(list_item)
        

    context = {
        'product':product,
        'user':user,
        'bigh':bigh,
        'stats':stats,
        'n':n
        
    }
    return render(request,'home/detail_page.html',context)

def Finall_Check (request,order_id) :
    order = Order.objects.get(id=order_id)
    cart = Cart(request)
    if request.method == 'POST' :
        form = Adrress_form(request.POST)
        if form.is_valid():
            adrress_save = form.save(commit=False)
            adrress_save.user = request.user
            adrress_save.order = order
            adrress_save.save()
            cart.clear()
        else:
            pass
    else:

        form = Adrress_form()
            
    return render (request,'home/finall_check.html' , {'form' :form ,'cart':cart})



def Add_Order (request) :
    cart = Cart(request)
    order = Order.objects.create(user=request.user)
    for item in cart :
        Orderitem.objects.create(user=request.user,order=order,product = item['product'], quantity = item['quantity'])
    return redirect('home:finall_check',order.id)

def Bookmark (request) :
    user = request.user
    print('dfhghsfdghgfdhgfdjhgdj')
    print(request.POST.get('post_id'))
    post = request.POST.get('post_id')
    product = Product.objects.get(id=post)
    bookmark,created=Bookamrk.objects.get_or_create(user=user,product=product)


    if not created:
        if bookmark.status == 'yes':
            bookmark.status = 'no'
        else:
            bookmark.status = 'yes'
    else:
        bookmark.status = 'yes'
    bookmark.save()

    return redirect ('home:detail_page_view',product.slug)


def filter_views (request,cat):

    if cat:
        categorys = Category.objects.get(slug=cat)
        products = Product.objects.filter(category=categorys)


    context = {
        'products':products,
    }

    return render(request,'home/filter_views.html',context)
    
