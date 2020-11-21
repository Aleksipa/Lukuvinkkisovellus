import pytest

from application import app


@pytest.fixture
def client():
    """Setup test client for Flask app"""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
