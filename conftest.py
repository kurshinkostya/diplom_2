import pytest
from data.endpoints import Endpoints, send_request
from data.user_data import User


@pytest.fixture(scope="function")
def create_user():
    """Фикстура: создаёт нового пользователя, возвращает данные и токен"""
    payload = User.create_data_user()
    login_data = payload.copy()
    del login_data["name"]

    response = send_request("POST", Endpoints.CREATE_USER, json=payload)

    if response.status_code != 200:
        print(f"⚠️ Не удалось создать пользователя: {response.status_code} {response.text}")

    token = response.json().get("accessToken")
    yield response, payload, login_data, token

    if token:
        send_request("DELETE", Endpoints.DELETE_USER, headers={"Authorization": token})

