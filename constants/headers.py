class Headers:


    GET_BOOKING_HEADER = {
     'Accept': 'application/json',
    }

    CREATE_BOOKING_HEADER = {
     'Content-Type': 'application/json',
     'Accept': 'application/json'
    }

    UPDATE_BOOKING_HEADER = {
     'Accept': 'application/json',
     'Content-Type': 'application/json',
     'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='
    }

    DELETE_BOOKING_HEADER = {
      'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='
    }