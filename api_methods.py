import allure
import requests
from urls import ApiUrls

class ApiMethods:
    @staticmethod
    @allure.step('Создание нового пользователя')
    def create_user(data):
        response = requests.post(ApiUrls.USER_CREATION, data=data)

        return response

    @staticmethod
    @allure.step('Удаление пользователя')
    def delete_user(token):
        requests.delete(ApiUrls.DELETE_USER + token)

    @staticmethod
    @allure.step('Логин пользователя')
    def login_user(data):
        response = requests.post(ApiUrls.LOGIN_USER, data=data)

        return response

    @staticmethod
    @allure.step('Изменение данных пользователя')
    def update_user_data(token, data):
        headers = {'Authorization': token}
        response = requests.patch(ApiUrls.UPDATE_USER_DATA, headers=headers, data=data)

        return response

    @staticmethod
    @allure.step('Создание заказа')
    def make_order(token, data):
        headers = {'Authorization': token}
        response = requests.post(ApiUrls.MAKE_ORDER, headers=headers, data=data)

        return response

    @staticmethod
    @allure.step('Получить информацию об ингредиентах')
    def ingredients():
        response = requests.get(ApiUrls.INGREDIENTS)

        return response

    @staticmethod
    @allure.step('Получить список заказов пользователя')
    def get_user_orders(token):
        headers = {'Authorization': token}
        response = requests.get(ApiUrls.GET_USERS_ORDERS, headers=headers)

        return response