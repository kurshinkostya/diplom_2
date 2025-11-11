import allure
import requests


class Urls:
    """Базовый URL стенда"""
    MAIN_URL = 'https://stellarburgers.education-services.ru'


class Endpoints:
    """API эндпоинты Stellar Burgers"""

    CREATE_USER = f"{Urls.MAIN_URL}/api/auth/register"
    LOGIN = f"{Urls.MAIN_URL}/api/auth/login"
    CHANGE_USER_DATA = f"{Urls.MAIN_URL}/api/auth/user"
    DELETE_USER = f"{Urls.MAIN_URL}/api/auth/user"
    MAKE_ORDER = f"{Urls.MAIN_URL}/api/orders"
    GET_ORDERS = f"{Urls.MAIN_URL}/api/orders"

    headers = {"Content-Type": "application/json"}


@allure.step("Отправляем {method} запрос на {url}")
def send_request(method, url, **kwargs):
    """Универсальный метод для запросов с логированием в Allure"""
    response = requests.request(method, url, **kwargs)
    if "json" in kwargs:
        allure.attach(str(kwargs["json"]), name="Request Body", attachment_type=allure.attachment_type.JSON)
    if "headers" in kwargs:
        allure.attach(str(kwargs["headers"]), name="Headers", attachment_type=allure.attachment_type.TEXT)
    allure.attach(response.text, name="Response", attachment_type=allure.attachment_type.JSON)
    return response
