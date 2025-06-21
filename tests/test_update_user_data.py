import allure
from helpers import CheckResponse
from data import ExpectedResponse
from api_methods import ApiMethods


class TestUpdateUserData:

    @allure.title('Проверка: можно изменить email авторизованного пользователя')
    @allure.description('Запрос PATCH на /api/auth/user с новым email и корректным токеном вернет 200 OK')
    def test_update_user_email_with_authorization_return_200_ok(self, create_user_valid_data, reg_values):
        token = create_user_valid_data.json()["accessToken"]
        new_email = f'abc_{reg_values["email"]}'
        new_user_data = {'email': new_email}

        response = ApiMethods.update_user_data(token, new_user_data)

        assert (response.status_code == ExpectedResponse.UPDATE_USER_DATA_SUCCESSFULLY['status_code']
                and response.json()['user']['email'] == new_email), "Ответ сервера не совпадает с ожидаемым"

    @allure.title('Проверка: можно изменить пароль авторизованного пользователя')
    @allure.description('Запрос PATCH на /api/auth/user с новым password и корректным токеном вернет 200 OK')
    def test_update_user_password_with_authorization_return_200_ok(self, create_user_valid_data, reg_values):
        token = create_user_valid_data.json()["accessToken"]
        new_password = f'abc_{reg_values["password"]}'
        new_user_data = {'password': new_password}

        update_response = ApiMethods.update_user_data(token, new_user_data)
        new_login_values = {
            "email": reg_values["email"],
            "password": new_password
        }
        login_response = ApiMethods.login_user(new_login_values)

        assert (update_response.status_code == ExpectedResponse.UPDATE_USER_DATA_SUCCESSFULLY['status_code']
                and login_response.status_code == ExpectedResponse.USER_LOGIN_SUCCESSFULLY['status_code']), "Ответ сервера не совпадает с ожидаемым"

    @allure.title('Проверка: можно изменить имя авторизованного пользователя')
    @allure.description('Запрос PATCH на /api/auth/user с новым name и корректным токеном вернет 200 OK')
    def test_update_user_name_with_authorization_return_200_ok(self, create_user_valid_data, reg_values):
        token = create_user_valid_data.json()["accessToken"]
        new_name = f'abc_{reg_values["name"]}'
        new_user_data = {'name': new_name}

        response = ApiMethods.update_user_data(token, new_user_data)

        assert (response.status_code == ExpectedResponse.UPDATE_USER_DATA_SUCCESSFULLY['status_code']
                and response.json()['user']['name'] == new_name), "Ответ сервера не совпадает с ожидаемым"

    @allure.title('Проверка: нельзя изменить email неавторизованного пользователя')
    @allure.description('Запрос PATCH на /api/auth/user с новым email и без авторизации вернет 401 Unauthorized')
    def test_update_user_email_with_no_authorization_return_401_unauthorized(self, reg_values):
        new_email = f'abc_{reg_values["email"]}'
        response = ApiMethods.update_user_data('', {'email': new_email})

        assert (response.status_code == ExpectedResponse.UPDATE_USER_DATA_NO_AUTHORIZATION['status_code']
                and response.json() == ExpectedResponse.UPDATE_USER_DATA_NO_AUTHORIZATION['response_text']), "Ответ сервера не совпадает с ожидаемым"

    @allure.title('Проверка: нельзя изменить email авторизованного пользователя, если новый email уже зарегистрирован')
    @allure.description('Запрос PATCH на /api/auth/user с email, который уже используется, и корректным токеном вернет 403 Forbidden')
    def test_update_user_email_with_email_that_is_already_used_return_403_forbidden(self, create_user_valid_data,
                                                                                    reg_values):
        # Первый пользователь (создан фикстурой)
        email1 = reg_values['email']  # Только email, токен не нужен

        # Второй пользователь
        reg_data2 = {
            'email': f'second_{reg_values["email"]}',
            'password': reg_values['password'],
            'name': reg_values['name']
        }
        user2 = ApiMethods.create_user(reg_data2)
        token2 = user2.json()['accessToken']

        # Пытаемся изменить email второго пользователя на email первого
        response = ApiMethods.update_user_data(token2, {'email': email1})

        assert (response.status_code == ExpectedResponse.UPDATE_USER_DATA_EMAIL_ALREADY_EXIST['status_code']
                and response.json() == ExpectedResponse.UPDATE_USER_DATA_EMAIL_ALREADY_EXIST['response_text']), "Ответ сервера не совпадает с ожидаемым"

        # Удаление второго пользователя
        ApiMethods.delete_user(token2)