import datetime
import json
import os

from requests import Response


class Logger:
    file_name = f"logs/log_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log"

    @classmethod
    def _write_log_to_file(cls, data):
        with open(cls.file_name, 'a', encoding='utf-8') as logger_file:
            logger_file.write(data)

    @classmethod
    def add_request(cls, url, data, headers, method):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')
        if data is not None:
            try:
                request_data = json.loads(data)
                data = json.dumps(request_data, indent=4, ensure_ascii=False)
            except Exception:
                pass

        data_to_add = f"\n-------\n"
        data_to_add += f"Test: {test_name}\n"
        data_to_add += f"\n"
        data_to_add += f"Request method: {method}\n"
        data_to_add += f"Request URL: {url}\n"
        data_to_add += f"Request data: {data}\n"
        data_to_add += f"Request headers: {headers}\n"
        data_to_add += f"\n"

        cls._write_log_to_file(data_to_add)

    @classmethod
    def add_response(cls, response: Response):
        cookies_as_dict = dict(response.cookies)
        headers_as_dict = dict(response.headers)
        try:
            response_data = json.loads(response.text)
            response_data_json = json.dumps(response_data, indent=4, ensure_ascii=False)
        except Exception:
            response_data_json = response.text

        data_to_add = f"Response code: {response.status_code}\n"
        data_to_add += f"Response text: {response_data_json}\n"
        data_to_add += f"Response headers: {headers_as_dict}\n"
        data_to_add += f"Response cookies: {cookies_as_dict}\n"
        data_to_add += f"-------\n"
        data_to_add += f"\n"

        cls._write_log_to_file(data_to_add)
