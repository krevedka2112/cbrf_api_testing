from http import HTTPStatus

import pytest
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta


def test_valfull_schema_validation(api_client):
    """Проверяем структуру ответа справочника валют и обязательные поля"""

    response = api_client.get_full_valutes()
    assert response.status_code == HTTPStatus.OK
    assert "application/xml" in response.headers["Content-Type"]

    root = ET.fromstring(response.content)
    items = root.findall("Item")
    assert len(items) > 0, "Список валют пуст!"

    for item in items:
        assert item.find("Name") is not None, "Отсутствует обязательное поле Name!"
        assert item.find("Nominal") is not None, "Отсутствует обязательное поле Nominal!"
        assert int(item.find("Nominal").text) > 0


def test_daily_rate_contains_usd(api_client):
    """Проверяем, что в выдаче курсов всегда присутствует USD с корректными данными"""

    response = api_client.get_daily_rates()
    assert response.status_code == HTTPStatus.OK

    root = ET.fromstring(response.content)
    usd_element = None
    for valute in root.findall("Valute"):
        if valute.attrib.get("ID") == "R01235":
            usd_element = valute
            break

    assert usd_element is not None, "Доллар США (ID R01235) не найден в ответе!"
    assert usd_element.find("CharCode").text == "USD"

    value_str = usd_element.find("Value").text.replace(",", ".")
    assert float(value_str) > 0.0, "Курс USD не может быть нулевым или отрицательным!"


def test_daily_rate_future_date(api_client):
    """Проверяем поведение API при запросе курса на дату из будущего"""

    future_date = (datetime.now() + timedelta(days=30)).strftime("%d/%m/%Y")
    response = api_client.get_daily_rates(date_req=future_date)
    assert response.status_code == HTTPStatus.OK

    root = ET.fromstring(response.content)
    actual_date = root.attrib.get("Date")
    assert actual_date != future_date, "API вернуло курс на дату из будущего!"


invalid_dates = ["2026-10-10",
                 "32/13/2026",
                 1234567890,
                 "valid_date"]
@pytest.mark.parametrize("invalid_date", invalid_dates)
def test_daily_rate_invalid_date_format(api_client, invalid_date):
    """date в запросе - неверного формата (YYYY-MM-DD), несуществующая дата, int-число, строка с символами"""

    response = api_client.get_daily_rates(date_req=invalid_date)
    assert response.status_code == HTTPStatus.OK

    root = ET.fromstring(response.content)
    assert root.tag == "ValCurs"

    expected_error_message = "Error in parameters"
    actual_error_message = root.text.strip() if root.text else ""
    assert actual_error_message == expected_error_message, f"Ожидалась {expected_error_message}, " \
                                                           f"но получено: {actual_error_message}"
