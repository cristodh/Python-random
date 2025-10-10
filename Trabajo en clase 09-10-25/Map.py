#Triplicar cada número de una lista usando map()
#Dada una lista de números, usa map() para crear una nueva lista
#con cada número triplicado.

lista = [1,3,6,10,42,3,7,22,99,38,40]

def multiplicacion():
    resultado = list(map(lambda x: x*3, lista))
    print(resultado)

multiplicacion()

