import allure
from data.endpoints import Endpoints, send_request
from data.user_data import User


@allure.suite("Авторизация пользователя")
class TestLogin:

    @allure.title("Успешная авторизация существующего пользователя")
    def test_login_user(self):
        response = send_request("POST", Endpoints.LOGIN, json=User.data_correct)
        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.title("Авторизация с некорректными данными")
    def test_login_user_error(self):
        response = send_request("POST", Endpoints.LOGIN, json=User.data_negative)
        assert response.status_code == 401
        assert response.json().get("success") is False
