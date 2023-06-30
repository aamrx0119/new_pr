from django.shortcuts import render
from accounts.models import MyUser
from home.models import Order

# Create your views here.
def Profile_dashboard (request) :
    user = request.user
    qs = MyUser.objects.get(id=user.id)
    order = Order.objects.filter(user=user)
    context = {
        'qs':qs,
        'order':order,
    
    }
    return render (request,'profiles/profile_dashboard.html',context)