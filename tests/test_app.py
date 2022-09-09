from bs4 import BeautifulSoup
import pytest

from app import create_app


def create_soup(html):
    return BeautifulSoup(html)


@pytest.fixture
def test_client():
    app = create_app("testing")

    with app.test_client() as test_client:

        return test_client


def test_index(test_client):
    """
    GIVEN a test client
    WHEN it makes a GET request to /
    THEN the right page is returned with a form
    """
    response = test_client.get('/')
    soup = create_soup(response.data)

    assert response.status_code == 200
    assert soup.select_one("h2").text == "Enter simulation data"
    assert soup.select_one("form") is not None


def test_plot(test_client):
    """
    GIVEN a test_client
    WHEN it makes a POST request
    THEN the visualization returned
    """
    data = {'probability': 0.5, 'prior': 'Uniform', 'param_a': 1, 'param_b': 1}
    response = test_client.post('/', data=data)
    soup = create_soup(response.data)

    assert response.status_code == 200
    assert soup.select_one("h2").text == "Coin flip simulation"
    assert soup.select_one("div.bk-root") is not None
