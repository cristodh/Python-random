class Libro:
    """Clase padre para representar un libro"""
    
    def __init__(self, titulo, autor, anio, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.disponible = disponible
    
    def mostrar_info(self):
        """Muestra los datos del libro"""
        estado = "Disponible" if self.disponible else "No disponible"
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año: {self.anio}")
        print(f"Estado: {estado}")
    
    def alquilar(self):
        """Cambia disponible a False"""
        if self.disponible:
            self.disponible = False
            print(f"El libro '{self.titulo}' ha sido alquilado.")
            return True
        else:
            print(f"El libro '{self.titulo}' no está disponible.")
            return False
    
    def devolver(self):
        """Cambia disponible a True"""
        if not self.disponible:
            self.disponible = True
            print(f"El libro '{self.titulo}' ha sido devuelto.")
            return True
        else:
            print(f"El libro '{self.titulo}' ya estaba disponible.")
            return False


class LibroImpreso(Libro):
    """Clase hija para libros impresos"""
    
    def __init__(self, titulo, autor, anio, num_paginas, disponible=True):
        super().__init__(titulo, autor, anio, disponible)
        self.num_paginas = num_paginas
    
    def mostrar_info(self):
        """Muestra los datos del libro impreso incluyendo número de páginas"""
        super().mostrar_info()
        print(f"Número de páginas: {self.num_paginas}")
        print(f"Tipo: Libro Impreso")


class LibroDigital(Libro):
    """Clase hija para libros digitales"""
    
    def __init__(self, titulo, autor, anio, tamano_mb, disponible=True):
        super().__init__(titulo, autor, anio, disponible)
        self.tamano_mb = tamano_mb
    
    def mostrar_info(self):
        """Muestra los datos del libro digital incluyendo tamaño en MB"""
        super().mostrar_info()
        print(f"Tamaño: {self.tamano_mb} MB")
        print(f"Tipo: Libro Digital")


class Biblioteca:
    """Clase para gestionar una biblioteca de libros"""
    
    def __init__(self, nombre="Mi Biblioteca"):
        self.nombre = nombre
        self.libros = []
    
    def agregar_libro(self, libro):
        """Agrega un libro a la biblioteca"""
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado a la biblioteca.")
    
    def mostrar_libros_disponibles(self):
        """Muestra todos los libros disponibles"""
        print(f"\n=== LIBROS DISPONIBLES EN {self.nombre.upper()} ===")
        libros_disponibles = [libro for libro in self.libros if libro.disponible]
        
        if not libros_disponibles:
            print("No hay libros disponibles en este momento.")
            return
        
        for i, libro in enumerate(libros_disponibles, 1):
            print(f"\n{i}. {libro.titulo}")
            libro.mostrar_info()
            print("-" * 40)
    
    def mostrar_todos_los_libros(self):
        """Muestra todos los libros de la biblioteca"""
        print(f"\n=== TODOS LOS LIBROS EN {self.nombre.upper()} ===")
        
        if not self.libros:
            print("No hay libros en la biblioteca.")
            return
        
        for i, libro in enumerate(self.libros, 1):
            print(f"\n{i}. {libro.titulo}")
            libro.mostrar_info()
            print("-" * 40)
    
    def buscar_libro_por_titulo(self, titulo):
        """Busca un libro por título"""
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None
    
    def pedir_libro(self, titulo):
        """Permite pedir (alquilar) un libro por título"""
        libro = self.buscar_libro_por_titulo(titulo)
        if libro:
            return libro.alquilar()
        else:
            print(f"No se encontró el libro '{titulo}' en la biblioteca.")
            return False
    
    def devolver_libro(self, titulo):
        """Permite devolver un libro por título"""
        libro = self.buscar_libro_por_titulo(titulo)
        if libro:
            return libro.devolver()
        else:
            print(f"No se encontró el libro '{titulo}' en la biblioteca.")
            return False