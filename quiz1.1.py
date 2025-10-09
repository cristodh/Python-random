datos = {
    "Nombre": "Chris",
    "Lugar": "San Jose",
    "Comida Favorita": "Pizza"
}

def ingresar_opcion ():
    while True:
        try:
            opcion = int(input(
                "\nBienvenido, seleccione la opcion que desea ejecutar:\n" 
                "1. Ingresar nueva Key al diccionario\n"
                "2. Editar Key existente\n" 
                "3. Eliminar Key existente\n"
                "4. Visualizar el diccionario completo\n"
                "5. Salir del programa\n"
                "Digite la opcion: "
                ))
            if 1 <= opcion <= 5:
                return opcion
            else:
                print("\nOpción fuera de rango. Intente de nuevo.")
        except ValueError:
            print("\nEntrada invalida. Por favor, ingrese un numero.")
                



def visualizar():
        print('----------------------------------')
        for key, value in datos.items():
            print(f"{key} ----> {value}")
        print('----------------------------------')


def editar_key():
    clave = input("\nIngresa la clave que quiera modificar: ")
    if clave in datos: #aqui se llama a la lista "datos"
        nuevo_valor = input (f"\nIngrese el nuevo valor para '{clave}: ")
        if nuevo_valor.strip() == "":
            print("\nEl valor no puede estar vacío. No se realizaron cambios.")
        else:
            datos[clave] = nuevo_valor
            print(f"\n'{clave}' ha sido actualizado.")
    else:
        print("\nLa clave no existe en el diccionario.")
    visualizar()

def eliminar_key():
    visualizar()
    clave = input("\nIngrese la clave que desea eliminar: ")
    if clave in datos:
        del datos[clave]
        print(f"\n'{clave}' ha sido eliminada del diccionario.")
    else:
        print("\nLa clave no existe. No se realizaron cambios.")
    visualizar()

def agregar_key():
    clave = input("\nIngrese la nueva clave: ") #aqui se pide si la clave
    if clave.strip() == "": #aqui se verifica si el input es vacio
        print("\nLa clave no puede estar vacía.")
        return
    if clave in datos: #aqui se verifica si la clave (key) ya existe en el diccionario (datos)
        print("\nLa clave ya existe. Use la opción de editar para modificar su valor.")
        return
    valor = input("\nIngrese el valor para la nueva clave: ") #aqui se pide el valor del key
    if valor.strip() == "": #aqui se verifica si el valor esta vacio
        print("\nEl valor no puede estar vacío.")
        return
    datos[clave] = valor #si ya se tiene el key y el valor se agrega
    print(f"\n'{clave}' ha sido agregada al diccionario.")
    visualizar()


#este es el bucle del menu del inicio
while True:
    opSelec = ingresar_opcion()
    if opSelec == 1:
        agregar_key()
    elif opSelec == 2:
        editar_key()
    elif opSelec == 3:
        eliminar_key()
    elif opSelec == 4:
        visualizar()
    elif opSelec == 5:
        print("\nPrograma finalizado.")
        break