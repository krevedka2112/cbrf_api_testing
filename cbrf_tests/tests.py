from locale import currency
import requests
import datetime
from xml.etree import ElementTree as ET

from . import api_builder


class TestClass:
    def test_xml_validation(self):
        api_misc = api_builder.request_daily_rates()
        fetched_data = ET.fromstring(api_misc)
        requested_date = fetched_data.get('Date')
        
        today = datetime.date.today()
        expected_date = today.strftime('%d.%m.%Y')
        
        assert requested_date == expected_date
        
    def test_daily_rates_rus(self):
        date_req = datetime.date(2024, 3, 2)
        
        api_misc = api_builder.request_daily_rates(date_req)
        fetched_data = ET.fromstring(api_misc)
        valute = fetched_data.find('Valute')
        
        valute_ID = valute.get('ID')
        valute_NumCode = valute.find('NumCode').text
        valute_Value = valute.find('Value').text
        
        test_ID = 'R01010'
        test_NumCode = '036'
        test_Value = '59,4582'
        
        assert (valute_ID, valute_NumCode, valute_Value) == (test_ID, test_NumCode, test_Value)
        
    def test_daily_rates_eng(self):
        date_req = datetime.date(2024, 3, 2)
        
        api_misc = api_builder.request_daily_rates(date_req, lang = 'eng')
        fetched_data = ET.fromstring(api_misc)
        valute = fetched_data.find('Valute')
        
        valute_ID = valute.get('ID')
        valute_NumCode = valute.find('NumCode').text
        valute_Name = valute.find('Name').text
        valute_Value = valute.find('Value').text
        
        test_ID = 'R01010'
        test_NumCode = '036'
        test_Name = 'Australian Dollar'
        test_Value = '59,4582'
        
        assert (valute_ID, valute_NumCode, valute_Name, valute_Value) == (test_ID, test_NumCode, valute_Name, test_Value)
        
    def test_dynamic_rates(self):
        date_req1 = datetime.date(2024, 3, 1)
        date_req2 = datetime.date(2024, 3, 10)
        currency_id = 'R01010'
        
        api_misc = api_builder.request_dynamic_rates(date_req1, date_req2, currency_id)
        fetched_data = ET.fromstring(api_misc)
        #record = fetched_data.find('Record')
        
        currency_Value = []
        for values in fetched_data.findall('Record'):
            value = values.find('Value').text
            currency_Value.append(value)
            
        test_Value = ['59,2201', '59,4582',
                      '59,5624', '59,2725',
                      '58,8483', '59,7675']
        
        assert (currency_Value) == (test_Value)