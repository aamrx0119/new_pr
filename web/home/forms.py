from django import forms 
from .models import Orderitem , Choice_test , Adrress_model



class Order_Item_form(forms.ModelForm):
    class Meta :
        model = Orderitem
        fields = ('quantity',)

class Adrress_form (forms.ModelForm):
    class Meta :
        model = Adrress_model
        exclude  = ('user','order')

class Choice_test_form(forms.ModelForm):
    class Meta :
        model = Choice_test
        fields = ('color',)

class quantity_form (forms.Form) :
    quantity1 = forms.IntegerField()

class Get_Products (forms.Form):
    CHOICE_BRAND = (
        ('Nike','Nike'),
        ('Adidas','Adidas'),
        ('Reebok','Reebok'),
    )

    CHOICE_Product = (
        ('clothes','clothes'),
        ('shoes','shoes'),
        ('Other','Other'),
    )
    Title = forms.ChoiceField(choices=CHOICE_BRAND)
    sex = forms.CharField(max_length=10)
    product= forms.ChoiceField(choices=CHOICE_Product)
    quantity= forms.IntegerField(min_value=1)
