#Condiciones
#edad < 13 = niño
#edad > = 13 && edad < 18 = Adolecente
#edad > = 18 && edad < 60 = Adulto
#edad > =60 = Adulto Mayor


def entrada_edad ():
    edad = int(input("Ingrese la edad a consultar: "))
    return edad

edad_ingresada = entrada_edad()

def clasificacion():

    if edad_ingresada < 13:
        print(f"Es un niño de {edad_ingresada}")
    elif edad_ingresada >= 13 and edad_ingresada < 18 :
        print(f"Es un Adolecente de {edad_ingresada}")
    elif edad_ingresada >= 18 and edad_ingresada < 60 :
        print(f"Es un Adulto de {edad_ingresada}")
    elif edad_ingresada >= 60 :
        print(f"Es un Adulto Mayor de {edad_ingresada}")

clasificacion()


