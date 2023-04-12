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

    def __init__(self):
        pass

    def request(self, req_type: HttpMethods, url: str, payload=None, headers=None):
        # parse payload
        payload = json.dumps(payload)


        print(f'HTTP REQUEST:\n'
              + f'Type: {req_type}\n'
              + f'URL: {url}\n'
              + f'Payload: {repr(payload)}')

        response = self.__REQ_TYPES[req_type](url=url, data=payload, headers=headers)
        status_code = f'{response.status_code} {response.reason}'
        if response.status_code == 200:
            print(f'HTTP RESPONSE: {status_code}')
        else:
            raise Exception(f'HTTP RESPONSE: {status_code}')
        return response.json()



