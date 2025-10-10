import random

respuesta_correcta = False
adivinado = True
def ingreso_input ():
    ingreso = input('\nIngresa el numero que estoy pensando del 1 al 100: ')
    if ingreso.isdigit():
        return int(ingreso)
    else:
        print('no letras')
        return


def numero_aleatorio ():
    numero_entero = random.randint(1,100)
    return numero_entero

data = ingreso_input()
num_random = numero_aleatorio()

while data != num_random:
    if data < num_random:
        print("\nEl numero que pienso es mas alto")
    elif data > num_random:
        print("\nEl numero que pienso es mas bajo")
    data = ingreso_input()  # Aquí ACTUALIZAS el valor de data

print("\n¡Felicidades! Adivinaste el número.")



