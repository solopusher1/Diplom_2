class ExpectedResponse:
    USER_CREATION_SUCCESSFULLY = {
        'status_code':200,
        'response_text_keys':['accessToken', 'refreshToken', 'success', 'user']
    }
    USER_CREATION_ALSO_EXIST = {
        'status_code':403,
        'response_text':{
            "success": False,
            "message": "User already exists"
        }
    }
    USER_CREATION_WITHOUT_REQUIRED_DATA = {
        'status_code': 403,
        'response_text': {
            "success": False,
            "message": "Email, password and name are required fields"
        }
    }
    USER_LOGIN_SUCCESSFULLY = {
        'status_code': 200,
        'response_text_keys': ['accessToken', 'refreshToken', 'success', 'user']
    }
    USER_LOGIN_INCORRECT_DATA = {
        'status_code': 401,
        'response_text': {
            "success": False,
            "message": "email or password are incorrect"
        }
    }
    UPDATE_USER_DATA_SUCCESSFULLY = {
        'status_code': 200,
        'response_text_keys': ['accessToken', 'refreshToken', 'success', 'user']
    }
    UPDATE_USER_DATA_NO_AUTHORIZATION = {
        'status_code': 401,
        'response_text': {
            "success": False,
            "message": "You should be authorised"
        }
    }
    UPDATE_USER_DATA_EMAIL_ALREADY_EXIST = {
        'status_code': 403,
        'response_text': {
            "success": False,
            "message": "User with such email already exists"
        }
    }
    MAKE_ORDER_SUCCESSFULLY = {
        'status_code': 200,
        'response_text_keys': ['name', 'order', 'success']
    }
    MAKE_ORDER_NO_INGREDIENTS = {
        'status_code': 400,
        'response_text': {
            "success": False,
            "message": "Ingredient ids must be provided"
        }
    }
    MAKE_ORDER_INVALID_INGREDIENT_ID = {
        'status_code': 500
    }
    GET_USER_ORDERS_SUCCESSFULLY = {
        'status_code': 200,
        'response_text_keys': ['success', 'orders', 'total', 'totalToday']
    }
    GET_USER_ORDERS_UNAUTHORIZED = {
        'status_code': 401,
        'response_text': {
            "success": False,
            "message": "You should be authorised"
        }
    }