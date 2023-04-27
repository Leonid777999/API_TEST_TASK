
from constants.payload_for_test_with_httpclient import Payload
from constants.endpoints.booking import BookingEndpoints




#     response_body = client.request(HttpMethods.PUT, Url.UPDATE.format(id=booking_id), Payload.PAYLOAD_FOR_UPDATE,
#                                    headers=Headers.UPDATE_BOOKING_HEADER, check_status_code=200)
#     assert response_body['firstname'] == 'Updated Name'
#     assert response_body['lastname'] == 'Updated Name'
#     assert response_body['totalprice'] == 200
#     assert response_body['depositpaid'] == False
#     assert response_body['bookingdates']['checkin'] == '2024-12-29'
#     assert response_body['bookingdates']['checkout'] == '2024-12-31'
#     assert response_body['additionalneeds'][0] == 'stone desert'
#     assert response_body['additionalneeds'][1] == 'bottle of water'
#
#     response_body = requests.delete(Url.DELETE.format(id=booking_id), headers=Headers.DELETE_BOOKING_HEADER)
#     assert response_body.status_code == 201
#     response_body = requests.get(Url.GET_BOOKING.format(id=booking_id), headers=Headers.GET_BOOKING_HEADER)
#     assert response_body.status_code == 404


def test(app):

    response_body = app.booking.create_booking(Payload.PAYLOAD_FOR_CREATE)
    booking_id = response_body['bookingid']
    app.booking.get_booking_list()
    app.booking.get_booking_by_id(BookingEndpoints.GET_BOOKING.format(id=booking_id), check_status_code=200)
    app.booking.update_booking(BookingEndpoints.UPDATE.format(id=booking_id), Payload.PAYLOAD_FOR_UPDATE)
    app.booking.delete_booking(BookingEndpoints.DELETE.format(id=booking_id))
    app.booking.get_booking_by_id(BookingEndpoints.GET_BOOKING.format(id=booking_id), check_status_code=404)
