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
            return "Division by zero"

        result = self._op1 / self._op2
        # zapisuje wynik "ładnie" dla integera
        return int(result) if result.is_integer() else result

    def subtract(self):
        return self._op1 - self._op2
