from log import Logger
from http_client import HttpClient, HttpMethods
from constants.endpoints.booking import BookingEndpoints



class Booking:

    log = Logger()

    def __init__(self, client: HttpClient):
        self.__client = client

    def create_booking(self, payload: dict):
        """
        create booking

        :param payload:
        :return:
        """
        self.log.info("Create booking from {url}".format(url=BookingEndpoints.CREATE))
        ret = self.__client.request(HttpMethods.POST, BookingEndpoints.CREATE, payload, check_status_code=200)
        self.log.debug("Booking from {url} was created".format(url=BookingEndpoints.CREATE))
        return ret

    def get_booking_list(self, payload=None,headers=None):
        """
        get list of bookings

        :return:
        """
        ret = self.__client.request(HttpMethods.GET, BookingEndpoints.GET_LIST, self.__client.headers,
                                    check_status_code=200)
        return ret

    def get_booking_by_id(self, url, check_status_code=None):
        """
        get specific booking by id

        :param check_status_code:
        :param url:
        :return:
        """
        return self.__client.request(HttpMethods.GET, url, self.__client.headers, check_status_code)

    def update_booking(self, url, payload: dict):
        """
        update specific booking

        :param url:
        :param payload:
        :return:
        """
        return self.__client.request(HttpMethods.PUT, url, payload, check_status_code=200)

    def delete_booking(self, url):
        """
        delete specific booking

        :param url:
        :return:
        """
        return self.__client.request(HttpMethods.DELETE, url, self.__client.headers, check_status_code=201)

