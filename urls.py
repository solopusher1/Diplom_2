class BaseUrls:
    BASE_URL = "https://stellarburgers.nomoreparties.site"

class ApiUrls:
    USER_CREATION = BaseUrls.BASE_URL + '/api/auth/register'
    DELETE_USER = BaseUrls.BASE_URL + '/api/auth/'
    LOGIN_USER = BaseUrls.BASE_URL + '/api/auth/login'
    UPDATE_USER_DATA = BaseUrls.BASE_URL + '/api/auth/user'
    MAKE_ORDER = BaseUrls.BASE_URL + '/api/orders'
    INGREDIENTS = BaseUrls.BASE_URL + '/api/ingredients'
    GET_USERS_ORDERS = BaseUrls.BASE_URL + '/api/orders'