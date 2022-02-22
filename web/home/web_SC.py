
from os import execvp, name
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import requests
from .models import Product



# Nike website (start)
class Web_Scraping():
    def __init__(self,brand,sex,product,quantity):
        self.brand=brand       
        self.sex=sex       
        self.product=product       
        self.quantity=quantity

    
    
    def Check_url (self) :
        if self.brand == 'Nike':
            if self.sex == 'man' :
                if self.product== 'clothes':
                    url = 'https://www.nike.com/w/mens-clothing-6ymx6znik1'
                elif self.product== 'shoes':
                    url = 'https://www.nike.com/w/mens-shoes-nik1zy7ok'

            elif self.sex == 'woman' :
                if self.product== 'clothes':
                    url = 'https://www.nike.com/w/womens-clothing-5e1x6z6ymx6'
                elif self.product== 'shoes':
                    url = 'https://www.nike.com/w/womens-shoes-5e1x6zy7ok'

        if self.brand == 'Adidas':
            if self.sex == 'man' :
                if self.product== 'clothes':
                    url = 'https://www.adidas.com/us/men-pants?start=0'
                elif self.product== 'shoes':
                    url = 'https://www.adidas.com/us/men-athletic_sneakers'

            elif self.sex == 'woman' :
                if self.product== 'clothes':
                    url = 'https://www.adidas.com/us/women-pants'
                elif self.product== 'shoes':
                    url = 'https://www.adidas.com/us/women-shoes'
        return url
        
        
                
    def Nike(self,category,tags):
            
            c=webdriver.Edge('E:\django projects\mywebsite\web\webscarping\msedgedriver.exe')
            c.get(self.Check_url())
            c.implicitly_wait(10)
            print('ok')
            try:
                c.find_element_by_class_name("hf-modal-btn-close").click()
            except Exception:
                print('The language is deffult value')
            finally:
                print('try block works ')

                names=[]
                sub=[]
                prices=[]


                product_num = c.find_elements_by_class_name('product-card__body')
                while len(product_num) <= self.quantity :
                    c.find_element_by_class_name('nav-version--v2').send_keys(Keys.PAGE_DOWN)
                    product_num = c.find_elements_by_class_name('product-card__body')

                print('*'*12)
                print('the quantity is right.....')


                all_p=c.find_elements_by_class_name('product-card__body')[:self.quantity]
                for a in all_p:

                    name=a.find_element_by_class_name('product-card__link-overlay')
                    price=a.find_element_by_class_name('product-price')
                    subtitle=a.find_element_by_class_name('product-card__subtitle')
                    names.append(name.text)
                    prices.append(price.text)
                    sub.append(subtitle.text)
                for i in range(len(all_p)) :
                    name_p= Product(name=names[i],information='no bio....',category=category,price=10,num_exists=1)
                    name_p.save()
                    name_p.tags.set(tags)

                
                print(len(names))
                print(len(sub))
                print(len(prices))
                print(names)
                print('0'*100)
                print(sub)
                print('0'*100)
                print(prices)
                print('0'*100)

class Adidas (Web_Scraping):
    
    def Adidas_clothes (self,category,tags) :

            c=webdriver.Edge('E:\django projects\mywebsite\web\webscarping\msedgedriver.exe')
            c.get(self.Check_url())
            c.implicitly_wait(10)
            try:
                c.find_element_by_class_name('gl-modal__close').click()
                Accept_lan = c.find_element_by_class_name('gl-cta--full-width')
                Accept_lan.click()
            except Exception :
                print('The language is deffult ')
            finally:
                products_C =c.find_elements_by_class_name('grid-item___3rAkS')[:self.quantity]
                fList=[]
                for i in products_C :
                    try:
                        c.find_element_by_class_name('theme-adidas').send_keys(Keys.PAGE_DOWN)
                        detail_product = i.find_element_by_class_name("glass-product-card__title")
                        fList.append(detail_product.text)
                        
                    except Exception:
                        print('ni ....')
                        # c.find_element_by_class_name('theme-adidas').send_keys(Keys.PAGE_DOWN)
        
                print(fList)

                print(len(products_C))

                for products in range(len(products_C)) :
                    name_p= Product(name=fList[products],information='no bio....',category=category,price=10,num_exists=1)
                    name_p.save()
                    name_p.tags.set(tags)


            input('pleas eenter any keys .... ')
            c.quit()



            
# Nike website (finish)
