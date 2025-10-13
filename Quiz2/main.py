from biblioteca import Libro, LibroImpreso, LibroDigital, Biblioteca

def main():
    """Función principal que demuestra el funcionamiento del sistema"""
    print("=== SISTEMA DE BIBLIOTECA ===\n")
    
    # Crea una biblioteca
    biblioteca = Biblioteca("Biblioteca Central")
    
    # Crea libros impresos
    libro1 = LibroImpreso("Cien años de soledad", "Gabriel García Márquez", 1967, 417)
    libro2 = LibroImpreso("Don Quijote de la Mancha", "Miguel de Cervantes", 1605, 863)
    libro3 = LibroImpreso("1984", "George Orwell", 1949, 328)
    
    # Crea libros digitales
    libro4 = LibroDigital("El Principito", "Antoine de Saint-Exupéry", 1943, 2.5)
    libro5 = LibroDigital("Fundación", "Isaac Asimov", 1951, 4.8)
    
    # Agrega libros a la biblioteca
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)
    biblioteca.agregar_libro(libro4)
    biblioteca.agregar_libro(libro5)
    
    print("\n" + "="*50)
    
    # Muestra todos los libros disponibles
    biblioteca.mostrar_libros_disponibles()
    
    print("\n" + "="*50)
    print("SIMULANDO PRÉSTAMOS Y DEVOLUCIONES...")
    
    # Pedir algunos libros
    print("\n--- Pidiendo libros ---")
    biblioteca.pedir_libro("1984")
    biblioteca.pedir_libro("El Principito")
    biblioteca.pedir_libro("Libro que no existe")  # Este no debería encontrarse
    
    # Mostrar libros disponibles después de los préstamos
    biblioteca.mostrar_libros_disponibles()
    
    # Devolver un libro
    print("\n--- Devolviendo libros ---")
    biblioteca.devolver_libro("1984")
    
    # Mostrar libros disponibles después de la devolución
    biblioteca.mostrar_libros_disponibles()
    
    print("\n" + "="*50)
    print("TODOS LOS LIBROS EN LA BIBLIOTECA:")
    biblioteca.mostrar_todos_los_libros()
    
    print("\n=== FIN DEL PROGRAMA ===")

# Ejecutar la función principal si este archivo se ejecuta directamente
if __name__ == "__main__":
    main()