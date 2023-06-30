from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.forms.forms import Form

from .models import MyUser
from django.contrib.auth.forms import PasswordResetForm,SetPasswordForm
from django.core.exceptions import ValidationError

from .models import MyUser



class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta :
        Model = MyUser
        fields = ('email','first_name','last_name','bio')


    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user



class UserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('email', 'password','first_name','bio','last_name','is_active','is_admin')



class user_login_form (forms.Form) :
    email = forms.EmailField(max_length=250)
    password = forms.CharField(widget=forms.PasswordInput)

class user_signup_form (forms.Form) :
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField(max_length=250)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)


    def clean_confirm_password(self) :
        p1 = self.cleaned_data.get('password')
        p2 = self.cleaned_data.get('confirm_password')
        if p1 and p2 and p1 != p2:
            raise ValidationError("Passwords don't match")
        return p2


class EmailValidationOnForgotPassword(PasswordResetForm):
    email = forms.EmailField(label='',widget=forms.EmailInput(attrs={'class':'form-control','style':"width: 9.25cm;","placeholder":"Email"}))
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not MyUser.objects.filter(email__iexact=email, is_active=True).exists():
            raise ValidationError("There is no user registered with the specified E-Mail address.")
        return email



class Changeeee(SetPasswordForm):
    new_password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control','style':"width: 9.25cm;","placeholder":"Password",}))
    new_password2 = forms.CharField(label='Confirm password',widget=forms.PasswordInput(attrs={'class':'form-control','style':"width: 9.25cm;","placeholder":"Confirm password"}))

