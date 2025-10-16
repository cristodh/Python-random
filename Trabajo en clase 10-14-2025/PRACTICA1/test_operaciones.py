from operaciones import sumar, restar, multiplicacion, dividir

def test_sumar():
    assert sumar(5, 3) == 8
    assert sumar(5.5, 3.2) == 8.7

def test_restar():
    assert restar(5, 3) == 2
    assert restar(5.5, 3.2) == 2.3

def test_multiplicacion():
    assert multiplicacion(5, 3) == 15
    assert multiplicacion(5.5, 2) == 11.0

def test_dividir():
    assert dividir(6, 3) == 2
    assert dividir(5.5, 2) == 2.75