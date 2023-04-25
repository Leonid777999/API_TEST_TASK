import pytest

from app import App
from http_client import HttpClient


@pytest.fixture(scope="session")
def client():
    return HttpClient()


@pytest.fixture(scope="session")
def app():
    return App()