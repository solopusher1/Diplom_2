import allure
from helpers import CheckResponse, random_make_order_body
from data import ExpectedResponse
from api_methods import ApiMethods

class TestMakeOrder:

    @allure.title('Проверка: авторизованный пользователь может создать заказ хотя бы с одним ингредиентом')
    @allure.description('Запрос POST на /api/orders с передачей токена и ингредиента вернет 200 OK')
    def test_make_order_with_ingredient_authorized_user_return_200_ok(self, reg_values):
        response = ApiMethods.create_user(reg_values)
        token = response.json()["accessToken"]
        make_order_response = ApiMethods.make_order(token, random_make_order_body())

        assert (make_order_response.status_code == ExpectedResponse.MAKE_ORDER_SUCCESSFULLY['status_code']
                and CheckResponse.check_make_order_response(make_order_response)), "Ответ сервера не совпадает с ожидаемым"
        ApiMethods.delete_user(token)

    @allure.title('Проверка: авторизованный пользователь не может создать заказ без хотя бы одного ингредиента')
    @allure.description('Запрос POST на /api/orders с передачей токена без ингредиентов вернет 400 Bad Request')
    def test_make_order_without_ingredients_authorized_user_return_400_bad_request(self, reg_values):
        response = ApiMethods.create_user(reg_values)
        token = response.json()["accessToken"]
        make_order_response = ApiMethods.make_order(token, {})

        assert (make_order_response.status_code == ExpectedResponse.MAKE_ORDER_NO_INGREDIENTS['status_code']
                and make_order_response.json() == ExpectedResponse.MAKE_ORDER_NO_INGREDIENTS['response_text']), "Ответ сервера не совпадает с ожидаемым"
        ApiMethods.delete_user(token)

    @allure.title('Проверка: неавторизованный пользователь может создать заказ хотя бы с одним ингредиентом')
    @allure.description('Запрос POST на /api/orders с передачей ингредиента и без передачи токена вернет 200 OK')
    def test_make_order_with_ingredient_non_authorized_user_return_200_ok(self):
        token = ''
        make_order_response = ApiMethods.make_order(token, random_make_order_body())

        assert (make_order_response.status_code == ExpectedResponse.MAKE_ORDER_SUCCESSFULLY['status_code']
                and CheckResponse.check_make_order_response(
                    make_order_response)), "Ответ сервера не совпадает с ожидаемым"

    @allure.title('Проверка: неавторизованный пользователь не может создать заказ без хотя бы одного ингредиента')
    @allure.description('Запрос POST на /api/orders без передачи токена и ингредиентов вернет 400 Bad Request')
    def test_make_order_without_ingredients_non_authorized_user_return_400_bad_request(self):
        token = ''
        make_order_response = ApiMethods.make_order(token, {})

        assert (make_order_response.status_code == ExpectedResponse.MAKE_ORDER_NO_INGREDIENTS['status_code']
                and make_order_response.json() == ExpectedResponse.MAKE_ORDER_NO_INGREDIENTS['response_text']), "Ответ сервера не совпадает с ожидаемым"

    @allure.title('Проверка: пользователь не может создать заказ, передав невалидный id ингредиента')
    @allure.description('Запрос POST на /api/orders с передачей невалидного id ингредиента вернет 500 Internal Server Error')
    def test_make_order_with_invalid_ingredient_id_return_500_internal_server_error(self):
        token = ''
        make_order_body = {
            'ingredients': ['invalid']
        }
        make_order_response = ApiMethods.make_order(token, make_order_body)
        assert make_order_response.status_code == ExpectedResponse.MAKE_ORDER_INVALID_INGREDIENT_ID['status_code'], "Ответ сервера не совпадает с ожидаемым"