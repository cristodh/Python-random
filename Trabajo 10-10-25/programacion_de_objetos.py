
# Importar las clases desde instrumentos.py
from instrumentos import Instrumento, Guitarra, Piano, Trompeta, Bateria, Violin

guitarra = Guitarra("Fender", "Cuerda", "Madera", False,6)
piano = Piano("Yamaha", "Cuerda", "Madera y metal", True)
trompeta = Trompeta("Bach", "Viento", "Latón", True)
bateria = Bateria("Pearl", "Percusión", "Madera y metal", False)
violin = Violin("Stradivarius", "Cuerda", "Madera", False)

guitarra.mostrar_info()
guitarra.tocar()
guitarra.afinar()
guitarra.rasguear()

piano.mostrar_info()
piano.tocar()
piano.presionar_teclas()

trompeta.mostrar_info()
trompeta.tocar()
trompeta.soplar()

bateria.mostrar_info()
bateria.tocar()
bateria.afinar()
bateria.golpear_tambores()

violin.mostrar_info()
violin.tocar()
violin.afinar()
violin.usar_arco()


