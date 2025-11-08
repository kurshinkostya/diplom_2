import allure
from data.endpoints import Urls, Endpoints, send_request
from data.ingredients_data import Ingredient


@allure.suite("Получение заказов пользователя")
class TestGetOrders:

    @allure.title("Получение заказов авторизованного пользователя")
    def test_get_orders_with_auth(self, create_user):
        token = {"Authorization": create_user[3]}
        send_request("POST", Endpoints.MAKE_ORDER, headers=token, json=Ingredient.correct_ingredients_data)
        response = send_request("GET", Endpoints.GET_ORDERS, headers=token)
        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.title("Попытка получить заказы без авторизации вызывает ошибку 401")
    def test_get_orders_not_auth(self):
        response = send_request("GET", Endpoints.GET_ORDERS)
        assert response.status_code == 401
        assert response.json()["message"] == "You should be authorised"
