import allure
from data.endpoints import Endpoints, send_request
from data.user_data import User


@allure.suite("Изменение данных пользователя")
class TestChangingUserData:

    @allure.title("Успешное изменение email авторизованного пользователя")
    def test_change_user_email_with_auth(self, create_user):
        token = {"Authorization": create_user[3]}
        payload = {"email": User.create_data_user()["email"]}
        response = send_request("PATCH", Endpoints.CHANGE_USER_DATA, headers=token, json=payload)
        assert response.status_code == 200
        assert response.json()["user"]["email"] == payload["email"]

    @allure.title("Успешное изменение имени авторизованного пользователя")
    def test_change_user_name_with_auth(self, create_user):
        token = {"Authorization": create_user[3]}
        payload = {"name": User.create_data_user()["name"]}
        response = send_request("PATCH", Endpoints.CHANGE_USER_DATA, headers=token, json=payload)
        assert response.status_code == 200
        assert response.json()["user"]["name"] == payload["name"]

    @allure.title("Изменение данных без авторизации вызывает ошибку 401")
    def test_change_user_data_not_auth(self):
        response = send_request("PATCH", Endpoints.CHANGE_USER_DATA, json=User.create_data_user())
        assert response.status_code == 401
        assert response.json()["message"] == "You should be authorised"
