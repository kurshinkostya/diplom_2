import pytest
from data.endpoints import Endpoints, send_request
from data.user_data import User


@pytest.fixture(scope="function")
def create_user():
    """Создаёт нового пользователя и возвращает токен"""
    payload = User.create_data_user()
    login_data = payload.copy()
    del login_data["name"]

    response = send_request("POST", Endpoints.CREATE_USER, json=payload)
    assert response.status_code == 200, f"Ошибка при создании пользователя: {response.text}"

    token = response.json()["accessToken"]
    yield response, payload, login_data, token

    send_request("DELETE", Endpoints.DELETE_USER, headers={"Authorization": token})
