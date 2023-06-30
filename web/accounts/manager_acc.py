from django.contrib.auth.models import (
    BaseUserManager, 
)

class MyUserManager(BaseUserManager):
    def create_user (self,email,password=None,):

        if not email :
            return ValueError('Email is required please enter a valid email')


        user = self.model(
            email=self.normalize_email(email),

        )

        
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser (self,email,first_name,last_name,password=None,):

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            
        )

        user.set_password(password)
        user.is_admin = True
        user.save(using=self._db)
        return user