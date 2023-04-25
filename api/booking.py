from constants.payload_for_test_with_httpclient import Payload
from constants.url import Url
from http_client import HttpClient, HttpMethods
from constants.endpoints.booking import BookingEndpoints
from constants.headers.booking import BookingHeaders


class Booking:

    def __init__(self, client: HttpClient):
        self.__client = client


    def create_booking(self, payload):
        """
        create booking

        :param payload:
        :return:
        """

        return self.__client.request(HttpMethods.POST, BookingEndpoints.CREATE, payload, check_status_code=200)

