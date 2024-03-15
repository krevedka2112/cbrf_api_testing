import requests
import datetime
from xml.etree import ElementTree as ET

from . import constants

def request_currencies_info():
    # example url: https://www.cbr.ru/scripts/XML_valFull.asp
    url = constants.api_url['info']
        
    response = requests.get()
    return response.content

def request_daily_rates(date_req: datetime.datetime = None, lang: str = 'rus'):
    # example url: https://www.cbr.ru/scripts/XML_daily.asp?date_req=02/03/2024
    url = constants.api_url['daily_rus']
    if lang == 'eng':
        url = constants.api_url['daily_eng']
        
    if date_req:
        str_date_req = format(date_req.strftime('%d/%m/%Y'))
        response = requests.get(f'{url}date_req={str_date_req}')
    else:
        response = requests.get(url)
            
    return response.content

def request_dynamic_rates(date_req1: datetime.datetime, date_req2: datetime.datetime,
                          currency_id: str):
    # example url: http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1=02/03/2024&date_req2=14/03/2024&VAL_NM_RQ=R01235
    str_date_req1 = format(date_req1.strftime('%d/%m/%Y'))
    str_date_req2 = format(date_req2.strftime('%d/%m/%Y'))
    
    add_url = f'date_req1={str_date_req1}&date_req2={str_date_req2}&VAL_NM_RQ={currency_id}'
    url = constants.api_url['dynamic'] + add_url
        
    response = requests.get(url)
    return response.content