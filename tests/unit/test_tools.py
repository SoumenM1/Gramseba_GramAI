from app.ai.tools.calculation_tools import CalculationTools


def test_add():
    assert CalculationTools.add(2, 3) == 5


def test_multiply():
    assert CalculationTools.multiply(3, 4) == 12