import requests
from utils.logger import Logger


class Client:
    def __init__(self, base_url):
        self.base_url = base_url

    def _send_request(self, method, path, params=None, data=None, headers=None):
        url = f"{self.base_url}{path}"
        headers = headers or {}

        Logger.add_request(url=url, data=data, headers=headers, method=method)
        response = requests.request(method=method, url=url, params=params, data=data, headers=headers)
        Logger.add_response(response)

        return response

    def get_daily_rates(self, date_req=None):
        params = {"date_req": date_req} if date_req else None

        return self._send_request("GET", "/scripts/XML_daily.asp", params=params)

    def get_full_valutes(self):
        return self._send_request("GET", "/scripts/XML_valFull.asp")
