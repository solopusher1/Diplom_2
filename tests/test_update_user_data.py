import allure

from tests.conftest import reg_values
from data import ExpectedResponse
from api_methods import ApiMethods

class TestUpdateUserData:

    @allure.title('Проверка: можно изменить email авторизованного пользователя')
    @allure.description('Запрос PATCH на /api/auth/user с новым email и корректным токеном вернет 200 OK')
    def test_update_user_email_with_authorization_return_200_ok(self, reg_values):
        reg_response = ApiMethods.create_user(reg_values)
        token = reg_response.json()["accessToken"]
        new_email = f'abc_{reg_values["email"]}'
        new_user_data = {
            'email': new_email
        }
        response = ApiMethods.update_user_data(token, new_user_data)

        assert (response.status_code == ExpectedResponse.UPDATE_USER_DATA_SUCCESSFULLY['status_code']
                and response.json()['user']['email'] == new_email), "Ответ сервера не совпадает с ожидаемым"
        ApiMethods.delete_user(token)

    @allure.title('Проверка: можно изменить пароль авторизованного пользователя')
    @allure.description('Запрос PATCH на /api/auth/user с новым password и корректным токеном вернет 200 OK')
    def test_update_user_password_with_authorization_return_200_ok(self, reg_values):
        reg_response = ApiMethods.create_user(reg_values)
        token = reg_response.json()["accessToken"]
        new_password = f'abc_{reg_values["password"]}'
        new_user_data = {
            'password': new_password
        }
        update_response = ApiMethods.update_user_data(token, new_user_data)
        new_login_values = {
            "email": reg_values["email"],
            "password": new_password
        }
        login_response = ApiMethods.login_user(new_login_values)
        assert (update_response.status_code == ExpectedResponse.UPDATE_USER_DATA_SUCCESSFULLY['status_code']
                and login_response.status_code == ExpectedResponse.USER_LOGIN_SUCCESSFULLY['status_code']), "Ответ сервера не совпадает с ожидаемым"
        ApiMethods.delete_user(token)

    @allure.title('Проверка: можно изменить имя авторизованного пользователя')
    @allure.description('Запрос PATCH на /api/auth/user с новым name и корректным токеном вернет 200 OK')
    def test_update_user_name_with_authorization_return_200_ok(self, reg_values):
        reg_response = ApiMethods.create_user(reg_values)
        token = reg_response.json()["accessToken"]
        new_name = f'abc_{reg_values["name"]}'
        new_user_data = {
            'name': new_name
        }
        response = ApiMethods.update_user_data(token, new_user_data)

        assert (response.status_code == ExpectedResponse.UPDATE_USER_DATA_SUCCESSFULLY['status_code']
                and response.json()['user']['name'] == new_name), "Ответ сервера не совпадает с ожидаемым"
        ApiMethods.delete_user(token)

    @allure.title('Проверка: нельзя изменить email неавторизованного пользователя')
    @allure.description('Запрос PATCH на /api/auth/user с новым email и без авторизации вернет 401 Unauthorized')
    def test_update_user_email_with_no_authorization_return_401_unauthorized(self, reg_values):
        new_email = f'abc_{reg_values["email"]}'
        new_user_data = {
            'email': new_email
        }
        token = ''
        response = ApiMethods.update_user_data(token, new_user_data)

        assert (response.status_code == ExpectedResponse.UPDATE_USER_DATA_NO_AUTHORIZATION['status_code']
                and response.json() == ExpectedResponse.UPDATE_USER_DATA_NO_AUTHORIZATION['response_text']), "Ответ сервера не совпадает с ожидаемым"

    @allure.title('Проверка: нельзя изменить пароль неавторизованного пользователя')
    @allure.description('Запрос PATCH на /api/auth/user с новым password и без авторизации вернет 401 Unauthorized')
    def test_update_user_password_with_no_authorization_return_401_unauthorized(self, reg_values):
        new_password = f'abc_{reg_values["password"]}'
        new_user_data = {
            'password': new_password
        }
        token = ''
        response = ApiMethods.update_user_data(token, new_user_data)

        assert (response.status_code == ExpectedResponse.UPDATE_USER_DATA_NO_AUTHORIZATION['status_code']
                and response.json() == ExpectedResponse.UPDATE_USER_DATA_NO_AUTHORIZATION[
                    'response_text']), "Ответ сервера не совпадает с ожидаемым"

    @allure.title('Проверка: нельзя изменить имя неавторизованного пользователя')
    @allure.description('Запрос PATCH на /api/auth/user с новым name и без авторизации вернет 401 Unauthorized')
    def test_update_user_name_with_no_authorization_return_401_unauthorized(self, reg_values):
        new_name = f'abc_{reg_values["name"]}'
        new_user_data = {
            'name': new_name
        }
        token = ''
        response = ApiMethods.update_user_data(token, new_user_data)

        assert (response.status_code == ExpectedResponse.UPDATE_USER_DATA_NO_AUTHORIZATION['status_code']
                and response.json() == ExpectedResponse.UPDATE_USER_DATA_NO_AUTHORIZATION[
                    'response_text']), "Ответ сервера не совпадает с ожидаемым"

    @allure.title('Проверка: нельзя изменить email авторизованного пользователя, если новый email уже зарегистрирован')
    @allure.description('Запрос PATCH на /api/auth/user с email, который уже используется, и корректным токеном вернет 403 Forbidden')
    def test_update_user_email_with_email_that_is_already_used_return_403_forbidden(self, reg_values):
        reg_data_1 = reg_values
        user_email_1 = reg_values['email']
        reg_response_1 = ApiMethods.create_user(reg_data_1)
        token_1 = reg_response_1.json()["accessToken"]

        user_email_2 = f'abc_{reg_values["email"]}'
        reg_data_2 = {
            "email": user_email_2,
            "password": reg_values["password"],
            "name": reg_values["name"]
        }
        reg_response_2 = ApiMethods.create_user(reg_data_2)
        token_2 = reg_response_2.json()["accessToken"]

        new_data_for_user_2 = {
            'email': user_email_1
        }
        update_response = ApiMethods.update_user_data(token_2, new_data_for_user_2)

        assert (update_response.status_code == ExpectedResponse.UPDATE_USER_DATA_EMAIL_ALREADY_EXIST['status_code']
                and update_response.json() == ExpectedResponse.UPDATE_USER_DATA_EMAIL_ALREADY_EXIST['response_text']), "Ответ сервера не совпадает с ожидаемым"
        ApiMethods.delete_user(token_1)
        ApiMethods.delete_user(token_2)