from calc import Calculator
import pytest
cal = Calculator()


def test_multiply_positive():
    x = 3
    y = 3
    res = 9
    assert cal.multiply(x,y) == res, f"Проверка умножения не пройдена {x} * {y} = {res}"

def test_multiply_negative():
    cal = Calculator()
    assert cal.multiply(3,3) !=10
    

def test_add_positive():
    x = 2
    y = 2
    res = 4
    assert cal.add(x,y) == res, f"Проверка сложения не пройдена {x} + {y} = {res}"

def test_adding_negative():
    cal = Calculator()
    assert cal.add(2,2) !=5


def test_divide_positive():
    x = 8
    y = 2
    res = 4
    assert cal.divide(x,y) == res, f"Проверка деления не пройдена {x} / {y} = {res}"

def test__divide_negative():
    cal = Calculator()
    assert cal.divide(8,2) !=5

def test_divide():
    cal = Calculator()
    assert cal.divide(8,0) in 'Ошибка!'

    

def test_subtract_positive():
    x = 4
    y = 2
    res = 2
    assert cal.subtract(x,y) == res, f"Проверка вычитание не пройдена {x} - {y} = {res}"

def test__subtract_negative():
    cal = Calculator()
    assert cal.subtract(4,2) !=1


