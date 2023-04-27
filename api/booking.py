from constants.payload_for_test_with_httpclient import Payload
from constants.url import Url
from http_client import HttpClient, HttpMethods
from constants.endpoints.booking import BookingEndpoints
from constants.headers.booking import BookingHeaders


class Booking:

    def __init__(self, client: HttpClient):
        self.__client = client


    def create_booking(self, payload: dict):
        """
        create booking

        :param payload:
        :return:
        """

        return self.__client.request(HttpMethods.POST, BookingEndpoints.CREATE, payload, check_status_code=200)

    def get_booking_list(self):
        """
        get list of bookings

        :return:
        """
        return self.__client.request(HttpMethods.GET, BookingEndpoints.GET_LIST, self.__client.headers,
                                     check_status_code=200)

    def get_booking_by_id(self, url):
        """
        get specific booking by id

        :param url:
        :return:
        """
        return self.__client.request(HttpMethods.GET, url, BookingHeaders.GET_BOOKING_HEADER,
                                     check_status_code=200)