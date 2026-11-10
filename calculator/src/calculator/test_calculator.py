import pytest

from .calculator import Calculator
from .calculator_app_web import app


@pytest.fixture
def client():
    return app.test_client()


# Testy kalkulatora
def test_sum():
    calc = Calculator(2, 3)
    assert calc.sum() == 5


def test_sum_float():
    calc = Calculator(2.5, 3.5)
    assert calc.sum() == 6.0


def test_subtract_float():
    calc = Calculator(4.8, 3.8)
    assert calc.subtract() == pytest.approx(1.0)


def test_subtract():
    calc = Calculator(4, 3)
    assert calc.subtract() == 1


def test_divide_float():
    calc = Calculator(10, 5)
    assert calc.divide() == 2


def test_divide_by_zero():
    calc = Calculator(10, 0)
    assert calc.divide() == "Division by zero"


def test_multiply_float():
    calc = Calculator(4.0, 2.5)
    assert calc.multiply() == 10


# Testy aplikacji webowej

def test_sum_web_app(client):
    response = client.get(
        "/calculate?op=sum&arg1=2&arg2=5"
    )

    assert response.status_code == 200
    assert response.get_data(as_text=True) == "2 + 5 = 7"


def test_subtract_web_app(client):
    response = client.get(
        "/calculate?op=sub&arg1=5&arg2=2"
    )

    assert response.status_code == 200
    assert response.get_data(as_text=True) == "5 - 2 = 3"


def test_multiply_web_app(client):
    response = client.get(
        "/calculate?op=mul&arg1=2&arg2=5"
    )

    assert response.status_code == 200
    assert response.get_data(as_text=True) == "2 * 5 = 10"


def test_division_web_app(client):
    response = client.get(
        "/calculate?op=div&arg1=10&arg2=2"
    )

    assert response.status_code == 200
    assert response.get_data(as_text=True) == "10 / 2 = 5"


def test_division_by_zero_web_app(client):
    response = client.get(
        "/calculate?op=div&arg1=5&arg2=0"
    )

    assert response.status_code == 400
    assert response.get_json() == {
        "error": "Division by zero"
    }


def test_missing_parameters_web_app(client):
    response = client.get(
        "/calculate?op=sum&arg1=2"
    )

    assert response.status_code == 400
    assert response.get_json() == {
        "error": "Missing or invalid parameters"
    }


def test_unknown_operation_web_app(client):
    response = client.get(
        "/calculate?op=unknown&arg1=2&arg2=5"
    )

    assert response.status_code == 400
    assert response.get_json() == {
        "error": "Unknown operation"
    }


# Testy parametryzowane
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (-1, -2, -3),
        (2.5, 3.5, 6.0),
    ]
)
def test_add_parametrized(a, b, expected):
    calc = Calculator(a, b)
    assert calc.sum() == expected
