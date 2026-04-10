from src.calculadora import sumar, restar, multiplicar, dividir
import pytest


# Test: suma de números positivos
def test_sumar_positivo():
    assert sumar(2, 3) == 5


# Test: suma de números negativos
def test_sumar_negativo():
    assert sumar(-2, -3) == -5


# Test: resta básica
def test_restar():
    assert restar(5, 3) == 2

# Test: resta con números negativos
def test_restar_negativo():
    assert restar(-5, -3) == -2

# Test: multiplicación de números positivos
def test_multiplicar_positivo():
    assert multiplicar(2, 3) == 6


# Test: multiplicación con número negativo
def test_multiplicar_negativo():
    assert multiplicar(-2, 3) == -6


# Test: división correcta
def test_dividir_normal():
    assert dividir(10, 2) == 5


# Test: verificar que dividir por cero lanza un error
def test_dividir_por_cero():
    with pytest.raises(ValueError):
        dividir(1, 0)