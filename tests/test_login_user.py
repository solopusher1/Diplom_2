
import allure
from helpers import CheckResponse
from data import ExpectedResponse
from api_methods import ApiMethods

class TestLoginUser:

    @allure.title('Проверка: пользователь может авторизоваться')
    @allure.description('Запрос POST на /api/auth/login с валидными данными вернет 200 OK')
    def test_user_login_with_valid_data_return_200_ok(self, create_user_valid_data):
        login_values = {
            "email": create_user_valid_data.json()["user"]["email"],
            "password": "qwerty"
        }
        login_response = ApiMethods.login_user(login_values)

        assert (login_response.status_code == ExpectedResponse.USER_LOGIN_SUCCESSFULLY['status_code']
                and CheckResponse.check_login_user_response(login_response)), \
                "Ответ сервера не совпадает с ожидаемым"

    @allure.title('Проверка: пользователь не может авторизоваться с неверным email')
    @allure.description('Запрос POST на /api/auth/login с неверным email вернет 401 Unauthorized')
    def test_user_login_with_incorrect_email_value_return_401_unauthorized(self, create_user_valid_data):
        login_values = {
            "email": f'incorrect_{create_user_valid_data.json()["user"]["email"]}',
            "password": "qwerty"
        }
        login_response = ApiMethods.login_user(login_values)

        assert (login_response.status_code == ExpectedResponse.USER_LOGIN_INCORRECT_DATA['status_code']
                and login_response.json() == ExpectedResponse.USER_LOGIN_INCORRECT_DATA['response_text']), "Ответ сервера не совпадает с ожидаемым"

    @allure.title('Проверка: пользователь не может авторизоваться с неверным паролем')
    @allure.description('Запрос POST на /api/auth/login с неверным password вернет 401 Unauthorized')
    def test_user_login_with_incorrect_password_value_return_401_unauthorized(self, create_user_valid_data):
        login_values = {
            "email": create_user_valid_data.json()["user"]["email"],
            "password": "incorrect_password"
        }
        login_response = ApiMethods.login_user(login_values)

        assert (login_response.status_code == ExpectedResponse.USER_LOGIN_INCORRECT_DATA['status_code']
                and login_response.json() == ExpectedResponse.USER_LOGIN_INCORRECT_DATA['response_text']), "Ответ сервера не совпадает с ожидаемым"

    @allure.title('Проверка: пользователь не может авторизоваться при отсутствии поля email в запросе')
    @allure.description('Запрос POST на /api/auth/login без поля email вернет 401 Unauthorized')
    def test_user_login_without_email_field_return_401_unauthorized(self, create_user_valid_data):
        login_values = {
            "password": "qwerty"
        }
        login_response = ApiMethods.login_user(login_values)

        assert (login_response.status_code == ExpectedResponse.USER_LOGIN_INCORRECT_DATA['status_code']
                and login_response.json() == ExpectedResponse.USER_LOGIN_INCORRECT_DATA['response_text']),"Ответ сервера не совпадает с ожидаемым"

    @allure.title('Проверка: пользователь не может авторизоваться при отсутствии поля password в запросе')
    @allure.description('Запрос POST на /api/auth/login без поля password вернет 401 Unauthorized')
    def test_user_login_without_password_field_return_401_unauthorized(self, create_user_valid_data):
        login_values = {
            "email": create_user_valid_data.json()["user"]["email"]
        }
        login_response = ApiMethods.login_user(login_values)

        assert (login_response.status_code == ExpectedResponse.USER_LOGIN_INCORRECT_DATA['status_code']
                and login_response.json() == ExpectedResponse.USER_LOGIN_INCORRECT_DATA['response_text']), "Ответ сервера не совпадает с ожидаемым"