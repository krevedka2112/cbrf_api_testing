currency_codes = {
    # https://www.cbr.ru/scripts/XML_valFull.asp
    'USD': 'R01235',
    'EUR': 'R01239',
}

url_protocol = 'https'
url_addres = 'www.cbr.ru'

url = f'{url_protocol}://{url_addres}'

api_url = {
    'info': f'{url}/scripts/XML_valFull.asp',
    'daily_rus': f'{url}/scripts/XML_daily.asp?',
    'daily_eng': f'{url}/scripts/XML_daily_eng.asp?',
    'dynamic': f'{url}/scripts/XML_dynamic.asp?',
}