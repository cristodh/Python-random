#Filtrar los números pares de una lista usando filter()
#Dada una lista de números, utiliza filter() para obtener una nueva lista que contenga únicamente los
#números pares.

lista = [1,3,6,10,42,3,7,22,99,38,40]

def num_pares ():
    pares=list(filter(lambda x : x % 2 == 0, lista))
    print (pares)

num_pares()