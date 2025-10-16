def restar (num,num2):
    if not isinstance(num,(int,float)) or not isinstance(num2,(int,float)):
        raise TypeError("Los datos deben de ser numeros")
    
    resultado = num - num2

    if resultado < 0:
        raise ValueError("El resultado no puede ser negativo")
    
    return resultado