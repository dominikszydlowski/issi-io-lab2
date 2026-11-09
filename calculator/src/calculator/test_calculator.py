import unittest
from .calculator import Calculator
from .calculator_app_web import app

class CalculatorTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_sum(self):
        calc = Calculator(2, 3)
        assert calc.sum() == 5

    def test_sum_float(self):
        calc = Calculator(2.5, 3.5)
        assert calc.sum() == 6.0

    def test_substract_float(self):
        calc = Calculator(4.8, 3.8)
        assert calc.subtract() == 1.0

    def test_substract(self):
        calc = Calculator(4, 3)
        assert calc.subtract() == 1

    def test_divide_float(self):
        calc = Calculator(10, 5)
        assert calc.divide() == 2

    def test_divide_by_zero(self):
        calc = Calculator(10, 0)
        assert  calc.divide() == 'Division by zero'

    def test_multiply_float(self):
        calc = Calculator(4.0, 2.5)
        assert calc.multiply() == 10

   # czesc dotyczaca aplikacji webowej

    def test_sum_web_app(self):
        response = self.client.get(
            "/calculate?op=sum&arg1=2&arg2=5"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_data(as_text=True),
            "2 + 5 = 7"
        )

    def test_subtract_web_app(self):
        response = self.client.get(
            "/calculate?op=sub&arg1=5&arg2=2"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_data(as_text=True),
            "5 - 2 = 3"
        )

    def test_multiply_web_app(self):
        response = self.client.get(
            "/calculate?op=mul&arg1=2&arg2=5"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_data(as_text=True),
            "2 * 5 = 10"
        )

    def test_division_web_app(self):
        response = self.client.get(
            "/calculate?op=div&arg1=10&arg2=2"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_data(as_text=True),
            "10 / 2 = 5"
        )

    def test_division_by_zero_web_app(self):
        response = self.client.get(
            "/calculate?op=div&arg1=5&arg2=0"
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.get_json(),
            {"error": "Division by zero"}
        )

    def test_missing_parameters_web_app(self):
        response = self.client.get(
            "/calculate?op=sum&arg1=2"
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.get_json(),
            {"error": "Missing or invalid parameters"}
        )

    def test_unknown_operation_web_app(self):
        response = self.client.get(
            "/calculate?op=unknown&arg1=2&arg2=5"
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.get_json(),
            {"error": "Unknown operation"}
        )
