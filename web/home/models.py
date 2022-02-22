from email.policy import default
from django.db import models
from django.utils.text import slugify
from .utils import get_random_code , Lir_price
from django.conf import settings
from django.urls import reverse
from accounts.models import MyUser

# Create your models here.


class Category (models.Model) :
    title = models.CharField(max_length=50)
    category_sub = models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True,related_name='sub_category')
    sub = models.BooleanField(default=False)
    slug = models.CharField(max_length=50)

    def __str__ (self) :
        return self.title

class Tags (models.Model) :
    title = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)

    
    def __str__ (self) :
        return str(self.title)



class Product (models.Model) :
    name = models.CharField(max_length=250)
    information = models.TextField(max_length=500)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,)
    tags = models.ManyToManyField(Tags)
    image = models.ImageField(default='avatar.png',upload_to='images/%Y/%M/%d/main')
    imag1 = models.ImageField(default='avatar.png',upload_to='images/%Y/%M/%d/1',)
    imag2 = models.ImageField(default='avatar.png',upload_to='images/%Y/%M/%d/2')
    image3 = models.ImageField(default='avatar.png',upload_to='images/%Y/%M/%d/3',)
    price = models.IntegerField()
    discount = models.IntegerField(null=True,blank=True)
    num_exists = models.PositiveIntegerField()
    exists = models.BooleanField(default=True)
    slug = models.SlugField(unique=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    __initial_name = None
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__initial_name = self.name

    class Meta :
        ordering = ('-created',)

    def get_absoulte_url(self):
        return reverse('home:detail_page_view',args=[self.slug,])

    def live_price(self):
        if self.discount:
            price = self.discount*Lir_price()
        else:
            price = self.price*Lir_price()
        return price
    
    


    def __str__(self) :
        return self.name


    def save(self,*args,**kwargs):
        to_slug = self.slug
        if self.slug == "" :
            to_slug = slugify(str(self.name))
            ex =Product.objects.filter(slug=to_slug).exists()
            while ex :
                to_slug = slugify(str(self.name)+''+str(get_random_code()))
                ex =Product.objects.filter(slug=to_slug).exists()
        self.slug = to_slug
        super().save(*args, **kwargs)

class Orderitem (models.Model) :
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='user_order',)
    order = models.ForeignKey('Order',on_delete=models.CASCADE,related_name='order_product',null=True,blank=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='user_product')
    quantity  = models.PositiveIntegerField()
    ordered = models.BooleanField(default=False)
    

    def __str__(self) :
        return f'{self.user} wants {self.product}--{self.quantity} '





class Order (models.Model) :
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='order_user')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    
    def __str__(self) :
        return f'{self.user} -- {self.paid} '


    def get_order_item_from_order (self) :
        return self.order_product.all()

    
    class Meta :
        ordering = ('-created',)




class Adrress_model (models.Model) :
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='adrress_order')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='adrress_order')
    name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    home_phone = models.PositiveIntegerField()
    postal_code = models.PositiveIntegerField()
    adrress = models.TextField(max_length=500)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__ (self) :
        return f'{self.order}/{self.adrress}/{self.phone}'







Color_choices = (
    ('red','red'),
    ('blue','blue'),
    ('green','green'),
)
class Choice_test (models.Model) :
    color = models.CharField(choices=Color_choices,max_length=5)



    def __str__ (self) :
        return self.color





STATUS_CHOICES = (
    ('yse','yes'),
    ('no','no'),
)
class Bookamrk (models.Model) :
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE,related_name='user_bookmark')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_bookmark')
    status = models.CharField(choices=STATUS_CHOICES,max_length=3,default='yes')


    def __str__(self) :
        return f"{self.user} add {self.product} to own bookmark === {self.status} "