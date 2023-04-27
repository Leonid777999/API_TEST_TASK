from api.booking import Booking
from http_client import HttpClient


class App:

    def __init__(self):
        self.__client = HttpClient(headers=
        {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='
        }
        )
        self.booking = Booking(self.__client)

