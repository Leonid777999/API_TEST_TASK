import pytest
from http_client import HttpClient


@pytest.fixture(scope="session")
def client():
    return HttpClient()
