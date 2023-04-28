
from constants.payload_for_test_with_httpclient import Payload


def test(app):
    app.booking.create_booking(Payload.PAYLOAD_FOR_CREATE)
