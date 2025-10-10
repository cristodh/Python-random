class Instrumento:
    def __init__(self, nombre, tipo, material, afinado):
        self.nombre = nombre 
        self.tipo = tipo  # si es de cuerda, percusion, aire, etc
        self.material = material
        self.afinado = afinado  #si o no

#accion de tocar
    def tocar(self):
        print(f"Estás tocando el {self.nombre}.")

#accion de afinar, si ya esta afinado, mostrar si ya lo esta
    def afinar(self):
        if not self.afinado:
            self.afinado = True
            print(f"{self.nombre} ha sido afinado.")
        else:
            print(f"{self.nombre} ya está afinado.")

    def mostrar_info(self):
        print(f"Instrumento: {self.nombre}, Tipo: {self.tipo}, Material: {self.material}, Afinado: {self.afinado}")

class Guitarra(Instrumento):
    def __init__(self, nombre, tipo, material, afinado,cant_cuerdas): #cada clase debe de tener sus atributos 
        super().__init__(nombre, tipo, material, afinado) #aqui solo irian los atributos del super class (padre)
        self.cant_cuerdas = cant_cuerdas #las que se añaden de mas, se declaran por aparte del super***

    def rasguear(self):
        print(f"Rasgueando la guitarra {self.nombre}.")

class Piano(Instrumento):
    def presionar_teclas(self):
        print(f"Presionando las teclas del piano {self.nombre}.")

class Trompeta(Instrumento):
    def soplar(self):
        print(f"Soplando la trompeta {self.nombre}.")

class Bateria(Instrumento):
    def golpear_tambores(self):
        print(f"Golpeando los tambores de la batería {self.nombre}.")

class Violin(Instrumento):
    def usar_arco(self):
        print(f"Usando el arco en el violín {self.nombre}.")
