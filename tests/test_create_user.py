import pytest
import allure
from data.endpoints import Endpoints, send_request
from data.user_data import User


@allure.suite("Создание пользователя")
class TestCreateUser:

    @allure.title("Создание нового пользователя")
    def test_create_new_user_success(self):
        data = User.create_data_user()
        response = send_request("POST", Endpoints.CREATE_USER, json=data)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание пользователя, который уже существует")
    def test_create_double_user_error(self):
        response = send_request("POST", Endpoints.CREATE_USER, json=User.data_double)
        assert response.status_code == 403
        assert "User already exists" in response.text

    @allure.title("Создание пользователя без обязательных полей")
    @pytest.mark.parametrize("user_data", [
        User.data_without_email,
        User.data_without_password,
        User.data_without_name
    ])
    def test_create_user_incorrect_data(self, user_data):
        response = send_request("POST", Endpoints.CREATE_USER, json=user_data)
        assert response.status_code == 403
        assert "Email, password and name are required fields" in response.text

