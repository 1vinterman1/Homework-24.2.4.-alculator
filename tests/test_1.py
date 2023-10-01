import pytest

from app.calc import Calculator

class Test_calc:
    def setup(self):
      self.calc= Calculator

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def test_деление(self):
        assert self.calc.division(self, 8, 2) == 4

    def test_сумма(self):
        assert self.calc.adding(self, 10, 2) == 12

    def test_вычитание(self):
        assert self.calc.subtraction(self, 26, 2) == 24

    def test_умножение(self):
        assert self.calc.multiply(self, 4, 4) == 16

    def teardown(self):
        print('Выполнение метода Teardown')
