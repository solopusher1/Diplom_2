import allure
from helpers import CheckResponse
from data import ExpectedResponse
from api_methods import ApiMethods

class TestGetUserOrders:

    @allure.title('Проверка: можно получить список заказов авторизованного пользователя')
    @allure.description('Запрос GET на /api/orders с передачей токена вернет 200 OK')
    def test_get_user_orders_with_authorization_return_200_ok(self, reg_values):
        user_create_response = ApiMethods.create_user(reg_values)
        token = user_create_response.json()["accessToken"]
        get_orders_response = ApiMethods.get_user_orders(token)
        assert (get_orders_response.status_code == ExpectedResponse.GET_USER_ORDERS_SUCCESSFULLY['status_code']
                and CheckResponse.check_get_user_orders_response(get_orders_response)), "Ответ сервера не совпадает с ожидаемым"
        ApiMethods.delete_user(token)

    @allure.title('Проверка: нельзя получить список заказов неавторизованного пользователя')
    @allure.description('Запрос GET на /api/orders без передачи токена вернет 401 Unauthorized')
    def test_get_user_orders_without_authorization_return_401_unauthorized(self):
        token = ''
        get_orders_response = ApiMethods.get_user_orders(token)
        assert (get_orders_response.status_code == ExpectedResponse.GET_USER_ORDERS_UNAUTHORIZED['status_code']
                and get_orders_response.json() == ExpectedResponse.GET_USER_ORDERS_UNAUTHORIZED['response_text']), "Ответ сервера не совпадает с ожидаемым"