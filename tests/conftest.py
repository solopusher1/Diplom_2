import pytest
import random

from api_methods import ApiMethods


@pytest.fixture(scope="function")
def reg_values():
    user_email = f'alex_ivanitskiy_20_{random.randint(1000,9999)}@yandex.ru'
    user_password = 'qwerty'
    user_name = 'Александр'
    return {
        "email": user_email,
        "password": user_password,
        "name": user_name
    }

@pytest.fixture(scope="function")
def create_user_valid_data(reg_values):
    response = ApiMethods.create_user(reg_values)

    yield response

    token = response.json()["accessToken"]
    ApiMethods.delete_user(token)