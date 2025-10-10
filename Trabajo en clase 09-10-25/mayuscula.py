#Convertir palabras en minúsculas a MAYÚSCULAS usando map()
#Dada una lista de palabras en minúsculas, usa map() para
#convertir todas las palabras a mayúsculas.

def texto_input ():
    texto = input ("Escribe el texto a convertir: ")
    return texto

def conv_mayus ():
        data = texto_input()
        mayus = ''.join(map(str.upper, data))
        print(mayus)
        opcion_usuario = input("Quiere continuar S/N: ")
        if opcion_usuario.lower() == "s":
              conv_mayus()
        else: print("Termino el programa")

conv_mayus()


