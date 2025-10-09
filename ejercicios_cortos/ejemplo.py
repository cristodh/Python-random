mi_lista = [1, 2, 3, 4, 5] # puede tener elementos repetidos
mi_dupla = (10, 20, 30)# no se puede modificar
mi_conjunto = {100, 200, 300} # no puede tener elementos repetidos
mi_diccionario = {
    "edad": "valor1", 
    "clave2": "valor2"
    } # aqui va el valor del objeto que seria mi_diccionario

#ejercicio 1

def saludar (nombre):
    print("Bienvenido", nombre)

persona = input("Digame su nombre rasta: ")


saludar(persona)

#Cree una funcion que se encargue de tomar dos notas y determine su promedio

def promedio ():
    nota1 = float(input("Ingrese la primera nota: "))
    nota2 = float(input("Ingrese la segunda nota: "))
    resultado = (nota1 + nota2) / 2
    return resultado


#Cree una funcion que permita mostrar el resultado del promedio al usuario, se debe mostrar el nombre del usuario y el promedio

def mostrar_promedio (nombre,promedio):
    print ("Hola ",nombre,", el promedio de su nota es ", promedio)

resultado_promedio = promedio()
mostrar_promedio(persona,resultado_promedio)

