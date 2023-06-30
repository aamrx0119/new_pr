
import requests
from bs4 import BeautifulSoup


class Web_Sc ():

    def __init__(self,sex,product,quantity):
        self.sex=sex
        self.product=product
        self.quantity=quantity
        

    
    def Nike (self):
        if self.sex=='man':
            if self.product=='clothes':
                rg = requests.get('https://www.nike.com/w/mens-clothing-6ymx6znik1')
            elif  self.product=='shoes':
                rg = requests.get('https://www.nike.com/w/mens-shoes-nik1zy7ok') 

        elif self.sex == 'woman':
            if self.product=='clothes':
                rg = requests.get('https://www.nike.com/w/womens-clothing-5e1x6z6ymx6')
            elif self.product == 'shoes' :
                rg = requests.get('https://www.nike.com/w/womens-shoes-5e1x6zy7ok')
        
            
        
        content = BeautifulSoup(rg.text,'html.parser') 
        result = content.find_all('div',class_='product-card__body')[:self.quantity]


        n=[]
        p=[]
        for card in result:
            name  = card.find('div',class_='product-card__title')
            n.append(name.text)
            price = card.find('div',{'data-test':'product-price'})
            p.append(price.text)

            
        print(n)
        print(p)
        print(len(n))

        print('finish....')

a=Web_Sc('man','shoes',5).Nike()





        
