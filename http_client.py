import json
import requests


class HttpMethods:
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'


class HttpClient:
    __session = requests.Session()
    __REQ_TYPES = {
        HttpMethods.GET: __session.get,
        HttpMethods.POST: __session.post,
        HttpMethods.PUT: __session.put,
        HttpMethods.DELETE: __session.delete
    }

    def __init__(self, headers: dict = None):
        self.headers = headers


    def request(self, req_type: HttpMethods, url: str, payload=None, check_status_code=None):
        # parse payload
        payload = json.dumps(payload)
        # update headers
        #if headers is not None:
        #    headers = self.__session.headers.copy().update(headers)

        print(f'HTTP REQUEST:\n'
              + f'Type: {req_type}\n'
              + f'URL: {url}\n'
              + f'Header:{self.headers}\n'
              + f'Payload: {repr(payload)}')

        response = self.__REQ_TYPES[req_type](url=url, data=payload, headers=self.headers)
        status_code = f'{response.status_code} {response.reason}'

        print(json.loads(response.text))
        print(f'HTTP RESPONSE: {status_code}')

        if check_status_code is not None:
            assert check_status_code == response.status_code

        try:
            return response.json()
        except requests.exceptions.JSONDecodeError:
            print("Json is empty")


