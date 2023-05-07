
from constants.payload_for_test_with_httpclient import Payload
from constants.endpoints.booking import BookingEndpoints


def test(app):

    response_body = app.booking.create_booking(Payload.PAYLOAD_FOR_CREATE)
    booking_id = response_body['bookingid']

    assert response_body['booking']['firstname'] == 'First Name'
    assert response_body['booking']['lastname'] == 'Last Name'
    assert response_body['booking']['totalprice'] == 100
    assert response_body['booking']['depositpaid'] == True
    assert response_body['booking']['bookingdates']['checkin'] == '2023-05-19'
    assert response_body['booking']['bookingdates']['checkout'] == '2023-05-21'
    assert response_body['booking']['additionalneeds'][0] == 'fruit garden'
    assert response_body['booking']['additionalneeds'][1] == '20 years old whiskey'


    app.booking.get_booking_list()
    response_body = app.booking.get_booking_by_id(BookingEndpoints.GET_BOOKING.format(id=booking_id),
                                                  check_status_code=200)
    assert response_body['firstname'] == 'First Name'
    assert response_body['lastname'] == 'Last Name'
    assert response_body['totalprice'] == 100
    assert response_body['depositpaid'] == True
    assert response_body['bookingdates']['checkin'] == '2023-05-19'
    assert response_body['bookingdates']['checkout'] == '2023-05-21'
    assert response_body['additionalneeds'][0] == 'fruit garden'
    assert response_body['additionalneeds'][1] == '20 years old whiskey'

    response_body = app.booking.update_booking(BookingEndpoints.UPDATE.format(id=booking_id),
                                               Payload.PAYLOAD_FOR_UPDATE)
    assert response_body['firstname'] == 'Updated Name'
    assert response_body['lastname'] == 'Updated Name'
    assert response_body['totalprice'] == 200
    assert response_body['depositpaid'] == False
    assert response_body['bookingdates']['checkin'] == '2024-12-29'
    assert response_body['bookingdates']['checkout'] == '2024-12-31'
    assert response_body['additionalneeds'][0] == 'stone desert'
    assert response_body['additionalneeds'][1] == 'bottle of water'

    app.booking.delete_booking(BookingEndpoints.DELETE.format(id=booking_id))
    app.booking.get_booking_by_id(BookingEndpoints.GET_BOOKING.format(id=booking_id), check_status_code=404)
