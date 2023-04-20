class Url:

    PREFIX = "https://restful-booker.herokuapp.com"
    GET_LIST = f"{PREFIX}/booking"
    GET_BOOKING = f"{PREFIX}/booking/{{id}}"
    CREATE = f"{PREFIX}/booking"
    UPDATE = f"{PREFIX}/booking/{{id}}"
    DELETE = f"{PREFIX}/booking/{{id}}"
