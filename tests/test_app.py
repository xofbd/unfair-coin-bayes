import pytest

from app.app import app


@pytest.fixture
def test_client():
    with app.test_client() as test_client:
        return test_client


def test_index(test_client):
    """
    GIVEN a test client
    WHEN it makes a GET request
    THEN the request is satisfied with the expected data
    """
    response = test_client.get('/')

    assert response.status_code == 200
    assert b"Enter the probability a coin turns up heads" in response.data


def test_plot(test_client):
    """
    GIVEN a test_client
    WHEN test client makes a POST request
    THEN request is satisfied with the expected data
    """
    data = {'probability': 0.5, 'prior': 'Uniform', 'param_a': 1, 'param_b': 1}
    response = test_client.post('/plot', data=data)

    assert response.status_code == 200
    assert b"Coin flip simulation" in response.data
