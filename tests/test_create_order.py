import allure
from data.endpoints import Endpoints, send_request
from data.ingredients_data import Ingredient


@allure.suite("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа авторизованным пользователем")
    def test_create_order_with_auth(self, create_user):
        token = {"Authorization": create_user[3]}
        response = send_request("POST", Endpoints.MAKE_ORDER, headers=token, json=Ingredient.correct_ingredients_data)
        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.title("Создание заказа без ингредиентов вызывает ошибку 400")
    def test_create_order_without_ingredients(self):
        response = send_request("POST", Endpoints.MAKE_ORDER)
        assert response.status_code == 400
        assert response.json()["message"] == "Ingredient ids must be provided"

    @allure.title("Создание заказа с некорректными ID ингредиентов вызывает 500")
    def test_create_order_invalid_ingredients(self):
        response = send_request("POST", Endpoints.MAKE_ORDER, json=Ingredient.incorrect_ingredients_data)
        assert response.status_code == 500
        assert "Internal Server Error" in response.text
