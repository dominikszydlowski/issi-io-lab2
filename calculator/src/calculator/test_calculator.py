import unittest
from .calculator import Calculator

class CalculatorTestCase(unittest.TestCase):

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
        assert  calc.divide() == 'Nie można dzielić przez zero'

    def test_multiply_float(self):
        calc = Calculator(4.0, 2.5)
        assert calc.multiply() == 10
