#cifrado
class CifradoCesar:
    def __init__(self):
        pass

    def cifrar(self,texto,desplazamiento=1):
        abecedario = 'abcdefghijklmnñopqrstuvwxyz' #incertamos el abecedario
        palabra_guardada = '' #aqui se va a ir guardando la palabra cifrada
        for letra in texto: #esto recorre la palabra
            if letra in abecedario: #preguntar si la letra esta en el abecedario
                pos_letra = abecedario.index(letra) #se le pregunta la posicion y se guarda la posicion
                nueva_pos = (pos_letra + desplazamiento) % len(abecedario) # ya sabiendo la posicion, se usa para asi saber el punto de partida para desplazarse
                #                                                           % hace que si se pasa del limite del abecedario vuelva al inicio
                #                                                           perro -> p tiene la posicion 15. Con un despalzamiento de 3, la nueva posicion es 18, que es la letra r
                palabra_guardada += abecedario[nueva_pos]
                # Se guarda con acumulacion la palabra cifrada. Es decir si la palabra es perro, se guarda primero r, y luego se van agregando las siguientes letras
            else:
                palabra_guardada += letra
                # si la letra y/o simbolo no esta en el abecedario, se queda igual
        print(palabra_guardada) 
        return palabra_guardada
            
        """
            Hay que recorrer la palabra (texto)
            Necesitamos saber el indice de cada letra
            a ese indice le sumamos el desplazamiento

            Como vamos guardando la palabra?

            Como validamos si la letra no esta en el abecedario
            para dejarlo normalito? -> , = .  
        """


# Instancias
cifrado = CifradoCesar()

cifrado.cifrar('perro',3)