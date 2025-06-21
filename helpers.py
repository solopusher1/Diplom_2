import random
from data import ExpectedResponse
from api_methods import ApiMethods

class CheckResponse:
    @staticmethod
    def check_create_user_response(response):
        response_dict_keys = ExpectedResponse.USER_CREATION_SUCCESSFULLY['response_text_keys']
        return all(key in response_dict_keys for key in list(response.json().keys()))

    @staticmethod
    def check_login_user_response(response):
        response_dict_keys = ExpectedResponse.USER_LOGIN_SUCCESSFULLY['response_text_keys']
        return all(key in response_dict_keys for key in list(response.json().keys()))

    @staticmethod
    def check_make_order_response(response):
        response_dict_keys = ExpectedResponse.MAKE_ORDER_SUCCESSFULLY['response_text_keys']

        return all(key in response_dict_keys for key in list(response.json().keys()))

    @staticmethod
    def check_get_user_orders_response(response):
        response_dict_keys = ExpectedResponse.GET_USER_ORDERS_SUCCESSFULLY['response_text_keys']

        return all(key in response_dict_keys for key in list(response.json().keys()))

def random_make_order_body():
    response = ApiMethods.ingredients()
    ingredient_id = response.json()['data'][random.randint(0,10)]['_id']
    make_order_body = {
        'ingredients' : [ingredient_id]
    }

    return make_order_body