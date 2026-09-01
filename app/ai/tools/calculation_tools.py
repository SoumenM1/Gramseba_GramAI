class CalculationTools:

    @staticmethod
    def add(a: float, b: float):
        return a + b

    @staticmethod
    def subtract(a: float, b: float):
        return a - b

    @staticmethod
    def multiply(a: float, b: float):
        return a * b

    @staticmethod
    def divide(a: float, b: float):

        if b == 0:
            raise ValueError(
                "Cannot divide by zero"
            )

        return a / b