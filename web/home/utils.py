import uuid
import requests
from bs4 import BeautifulSoup

def get_random_code ():
    code = str(uuid.uuid4())[:8].replace('-','').lower()
    return code


def Lir_price():
    req = requests.get('https://www.tgju.org/profile/price_try')
    result = BeautifulSoup(req.text,'html.parser')
    r=result.find('span',{'data-col':'info.last_trade.PDrCotVal'})
    price = str((r.text))
    x=price.replace(',','')
    n=(int(x))
    return n


