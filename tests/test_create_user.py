import allure
import pytest

from helpers import CheckResponse
from data import ExpectedResponse
from api_methods import ApiMethods

class TestCreateUser:

    @allure.title('Проверка: можно создать пользователя')
    @allure.description('Запрос POST на /api/auth/register с валидными данными вернет 200 OK')
    def test_user_creation_with_valid_data_return_200_ok(self, reg_values):
        response = ApiMethods.create_user(reg_values)

        assert (response.status_code == ExpectedResponse.USER_CREATION_SUCCESSFULLY['status_code']
                and CheckResponse.check_create_user_response(response)), "Ответ сервера не совпадает с ожидаемым"

        token = response.json()["accessToken"]
        ApiMethods.delete_user(token)


    @allure.title('Проверка: нельзя создать пользователя, который уже зарегистрирован')
    @allure.description('Повторный запрос POST на /api/auth/register с теми же данными вернет 403 Forbidden')
    def test_user_creation_with_the_same_data_return_403_forbidden(self, reg_values):
        ApiMethods.create_user(reg_values)
        response = ApiMethods.create_user(reg_values)

        assert (response.status_code == ExpectedResponse.USER_CREATION_ALSO_EXIST['status_code']
                and response.json() == ExpectedResponse.USER_CREATION_ALSO_EXIST['response_text']), "Ответ сервера не совпадает с ожидаемым"

    @allure.title('Проверка: нельзя создать пользователя, не передав значение для обязательного поля')
    @allure.description('Запрос POST на /api/auth/register без значения для обязательного поля вернет 403 Forbidden')
    @pytest.mark.parametrize('field_name', ['email', 'password', 'name'])
    def test_user_creation_without_value_for_required_field_return_403_forbidden(self, reg_values, field_name):
        reg_data_without_required_value = reg_values
        reg_data_without_required_value[field_name] = ''
        response = ApiMethods.create_user(reg_data_without_required_value)

        assert (response.status_code == ExpectedResponse.USER_CREATION_WITHOUT_REQUIRED_DATA['status_code']
                and response.json() == ExpectedResponse.USER_CREATION_WITHOUT_REQUIRED_DATA['response_text']), "Ответ сервера не совпадает с ожидаемым"


    @allure.title('Проверка: нельзя создать пользователя при отсутствии в запросе обязательного поля')
    @allure.description('Запрос POST на /api/auth/register без обязательного поля вернет 403 Forbidden')
    @pytest.mark.parametrize('field_name', ['email', 'password', 'name'])
    def test_user_creation_without_required_field_return_403_forbidden(self, reg_values, field_name):
        reg_data_without_required_field = reg_values.pop(field_name)
        response = ApiMethods.create_user(reg_data_without_required_field)

        assert (response.status_code == ExpectedResponse.USER_CREATION_WITHOUT_REQUIRED_DATA['status_code']
                and response.json() == ExpectedResponse.USER_CREATION_WITHOUT_REQUIRED_DATA['response_text']), "Ответ сервера не совпадает с ожидаемым"