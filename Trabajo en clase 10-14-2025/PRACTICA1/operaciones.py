def restar(num, num2):
    if not isinstance(num, (int, float)) or not isinstance(num2, (int, float)):
        raise TypeError("Los datos deben de ser numeros")

    resultado = num - num2

    return resultado


def sumar(num, num2):
    if not isinstance(num, (int, float)) or not isinstance(num2, (int, float)):
        raise TypeError("Los datos deben de ser numeros")

    resultado = num + num2

    return resultado


def multiplicacion(num, num2):
    if not isinstance(num, (int, float)) or not isinstance(num2, (int, float)):
        raise TypeError("Los datos deben de ser numeros")

    resultado = num * num2

    if num or num2 == 0:
        raise ValueError("Para obtener el producto, los numero dados deben de ser mayor a '0'")

    return resultado


def dividir(num, num2):
    if not isinstance(num, (int, float)) or not isinstance(num2, (int, float)):
        raise TypeError("Los datos deben de ser numeros")

    resultado = num / num2

    if num or num2 == 0:
        raise ValueError("El divisor ni el dividendo pueden ser cero")

    return resultado


