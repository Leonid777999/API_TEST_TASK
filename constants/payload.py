import json


class Payload:

    PAYLOAD_FOR_CREATE = json.dumps({
     'firstname': 'First Name',
     'lastname': 'Last Name',
     'totalprice': 100.00,
     'depositpaid': True,
     'bookingdates':
     {
      'checkin': '2023-05-19',
      'checkout': '2023-05-21'
     },
     'additionalneeds':
     (
      'fruit garden', '20 years old whiskey'
     )
    })

    PAYLOAD_FOR_UPDATE = json.dumps({
     'firstname': 'Updated Name',
     'lastname': 'Updated Name',
     'totalprice': 200.00,
     'depositpaid': False,
     'bookingdates': {
       'checkin': '2024-12-29',
       'checkout': '2024-12-31'
      },
     'additionalneeds': (
       'stone desert', 'bottle of water'
      )
     })
