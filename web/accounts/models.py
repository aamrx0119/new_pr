from django.db import models
from django.contrib.auth.models import (
     AbstractBaseUser
)
from django.db.models.fields import TextField
from .manager_acc import MyUserManager


# Create your models here.

class MyUser (AbstractBaseUser) :
    email = models.EmailField(unique=True,max_length=250)
    bio = models.TextField(max_length=450,null=True,blank=True)
    first_name = models.CharField(max_length=100,blank=True,null=True)
    last_name = models.CharField(max_length=100,blank=True,null=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = MyUserManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    def __str__(self) :
        return f'{self.first_name} {self.last_name}--{self.email}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


    def get_user_products (self) :
        return self.order_user.all()
