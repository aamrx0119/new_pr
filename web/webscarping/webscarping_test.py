
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from home.models import Product




# Nike website (start)
# def Nike_PR(category,tags):
#     url = 'https://www.nike.com/w/womens-clothing-5e1x6z6ymx6'
#     rg = requests.get(url)
#     content = BeautifulSoup(rg.text,'html.parser') 
#     result = content.find_all('div',class_='product-card__body')


#     n=[]
#     p=[]
#     for card in result:
#         name  = card.find('div',class_='product-card__title')
#         n.append(name.text)
#         price = card.find('div',{'data-test':'product-price'})
#         p.append(price.text)

        
#     print(n)
#     print(p)

#     for i in range(len(result)):
#         name_p= Product(name=n[i],information='no bio....',category=category,price=10,num_exists=1)
#         name_p.save()
#         name_p.tags.set(tags)
#     print('finish....')
# Nike website (finish)
# ==================================================================================================================
# def Sel_nike(category,tags):
#     url = 'https://www.nike.com/w/womens-clothing-5e1x6z6ymx6'
#     c=webdriver.Edge('E:\django projects\mywebsite\web\webscarping\msedgedriver.exe')
#     c.get(url)
#     time.sleep(10)
#     print('ok')
#     try:
#         c.find_element_by_class_name("hf-modal-btn-close").click()
#     except Exception:
#         print('The language is deffult value')
#     finally:
#         print('try block works ')
#         # f=c.find_elements_by_class_name('product-card__link-overlay')
#         # p=c.find_elements_by_class_name('product-price')

#         # prices=[]
#         # quantity=0
#         # for m in p :
#         #     quantity=quantity+1
#         #     if quantity>3:
#         #         break
#         #     else:
#         #         prices.append(m.text)  

#         # number=0
#         # products = []

#         # for x in f :
#         #     number=number+1
#         #     if number>3:
#         #         break
#         #     else:
#         #         products.append(x.text)
        
#         names=[]
#         sub=[]
#         prices=[]


#         product_num = c.find_elements_by_class_name('product-card__body')
#         while len(product_num) <= 30 :
#             c.find_element_by_class_name('nav-version--v2').send_keys(Keys.PAGE_DOWN)
#             product_num = c.find_elements_by_class_name('product-card__body')

#         print('*'*12)
#         print('the quantity is right.....')


#         all_p=c.find_elements_by_class_name('product-card__body')[:30]
#         for a in all_p:

#             name=a.find_element_by_class_name('product-card__link-overlay')
#             price=a.find_element_by_class_name('product-price')
#             subtitle=a.find_element_by_class_name('product-card__subtitle')
#             names.append(name.text)
#             prices.append(price.text)
#             sub.append(subtitle.text)
#         for i in range(len(all_p)) :
#             name_p= Product(name=names[i],information='no bio....',category=category,price=10,num_exists=1)
#             name_p.save()
#             name_p.tags.set(tags)

        
#         print(len(names))
#         print(len(sub))
#         print(len(prices))
#         print(names)
#         print('0'*100)
#         print(sub)
#         print('0'*100)
#         print(prices)
#         print('0'*100)

            


    

            
                
        # print('='*100)
        # for x in products:
        #     print(x)
            
                
        # print('+'*100)
        # for m in prices:
        #     print(m)
            
        # input('enter any keys')
        # c.quit()      
                




    # for q in c.find_elements_by_class_name('product-card css-1kkp26o css-z5nr6i css-11ziap1 css-14d76vy css-dpr2cn product-grid__card '):
    #     print('find')













    # rg = requests.get('https://en.wikipedia.org/wiki/List_of_Game_of_Thrones_episodes')
    # rgb=BeautifulSoup(rg.text,'html.parser')
    # #header
    # content = rgb.find('tr',{'style':'color:white;text-align:center'}).find_all('th',{'scope':'col'})
    # header=[]
    # for x in content:
    #     header.append(x.text)
    # print(header)

    # #values
    # content2=rgb.find_all('table',class_='wikiepisodetable')

    # value=[]
    # m=[]
    # episodes = []
    # for v in content2:
    #     val=v.find_all('tr',class_='vevent')
    #     for h in val:
    #         value.append(h.text)
    # for name in value:
    #     m.append(name)

    # print(m[72])

        
        # for h in val:
        #     h.findAll('th')
        #     for n in h:
        #         for h in range(len(val)) :
        #             value.append(n.text)
            # for x in value:
            #      print(x)
            #      print('*********************************')

    # print(value)


        




















    # START
    # result = content.findAll('div',class_='product-card__titles')
    # result_price = content.findAll('div',class_='product-price')

    # header_price = []
    # for i in result_price:
    #     header_price.append(i.text)


    # for price in header_price:
    #     print (price)

    # header = []
    # for i in result:
    #     header.append(i.text)

    # # print(header)

    # for name in header:
    #     print (name)

    # print('8'*100)
    # print(header[0])
    # FINISH







    # url = 'https://en.wikipedia.org/wiki/List_of_Game_of_Thrones_episodes'
    # content1 = requests.get(url)
    # content2 = BeautifulSoup(content1.text,'html.parser') 
    # epTable = content2.findAll('table',class_="wikiepisodetable")





    # episodes=[]
    # for table in epTable:
    #     headers = []
    #     rows = table.findAll('tr')

    #     for header in table.find('tr').findAll('th'):
    #         headers.append(header.text)
            
        
    #     for row in table.findAll('tr')[1:] :
    #         values = []
    #         for col in row.findAll(['th','td']):
    #             values.append(col.text)
    #             if values:
    #                 episodedict = {headers[i]:values[i] for i in range(len(values))}
    #                 episodes.append(episodedict)

    # for ep in episodes:
    #      print(ep)

        
