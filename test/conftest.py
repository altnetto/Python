import pytest
from TU101.app import create_app

@pytest.fixture(scope="module")
def app():
    return create_app()