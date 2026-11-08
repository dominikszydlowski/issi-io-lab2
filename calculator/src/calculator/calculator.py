class Calculator:
    def __init__(self, op1: float, op2: float):
        self._op1 = op1
        self._op2 = op2

    def sum(self):
        return self._op1 + self._op2

    def multiply(self):
        return self._op1 * self._op2

    def divide(self):
        if self._op2 == 0:
            return "Nie można dzielić przez zero"
        return self._op1 / self._op2

    def subtract(self):
        return self._op1 - self._op2
