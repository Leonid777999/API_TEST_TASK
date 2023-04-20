import requests
from http_client import HttpMethods
from constants.url import Url
from constants.payload_for_test_with_httpclient import Payload
from constants.headers import Headers


def test_check_booking_api(client):
    response_body = client.request(HttpMethods.POST, Url.CREATE, Payload.PAYLOAD_FOR_CREATE,
                                   headers=Headers.CREATE_BOOKING_HEADER, check_status_code=200)
    booking_id = response_body['bookingid']
    assert response_body['booking']['firstname'] == 'First Name'
    assert response_body['booking']['lastname'] == 'Last Name'
    assert response_body['booking']['totalprice'] == 100
    assert response_body['booking']['depositpaid'] == True
    assert response_body['booking']['bookingdates']['checkin'] == '2023-05-19'
    assert response_body['booking']['bookingdates']['checkout'] == '2023-05-21'
    assert response_body['booking']['additionalneeds'][0] == 'fruit garden'
    assert response_body['booking']['additionalneeds'][1] == '20 years old whiskey'

    response_body = client.request(HttpMethods.GET, Url.GET_BOOKING.format(id=booking_id),
                                   headers=Headers.GET_BOOKING_HEADER, check_status_code=200)
    assert response_body['firstname'] == 'First Name'
    assert response_body['lastname'] == 'Last Name'
    assert response_body['totalprice'] == 100
    assert response_body['depositpaid'] == True
    assert response_body['bookingdates']['checkin'] == '2023-05-19'
    assert response_body['bookingdates']['checkout'] == '2023-05-21'
    assert response_body['additionalneeds'][0] == 'fruit garden'
    assert response_body['additionalneeds'][1] == '20 years old whiskey'

    response_body = client.request(HttpMethods.PUT, Url.UPDATE.format(id=booking_id), Payload.PAYLOAD_FOR_UPDATE,
                                   headers=Headers.UPDATE_BOOKING_HEADER, check_status_code=200)
    assert response_body['firstname'] == 'Updated Name'
    assert response_body['lastname'] == 'Updated Name'
    assert response_body['totalprice'] == 200
    assert response_body['depositpaid'] == False
    assert response_body['bookingdates']['checkin'] == '2024-12-29'
    assert response_body['bookingdates']['checkout'] == '2024-12-31'
    assert response_body['additionalneeds'][0] == 'stone desert'
    assert response_body['additionalneeds'][1] == 'bottle of water'

    response_body = requests.delete(Url.DELETE.format(id=booking_id), headers=Headers.DELETE_BOOKING_HEADER)
    assert response_body.status_code == 201
    response_body = requests.get(Url.GET_BOOKING.format(id=booking_id), headers=Headers.GET_BOOKING_HEADER)
    assert response_body.status_code == 404
