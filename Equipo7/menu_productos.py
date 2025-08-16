from tabulate import tabulate
from lectura_productos import leer_productos

def mostrar_menu():
    while True:
        print("\n=== Menú de Productos ===")
        print("1. Ver todos los productos")
        print("2. Buscar producto")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            productos = leer_productos()
            print(tabulate(productos, headers="keys", tablefmt="fancy_grid"))
        
        elif opcion == "2":
            termino = input("Ingresa el nombre o ID del producto: ").strip().lower()
            productos = leer_productos()
            encontrados = [p for p in productos if termino in str(p["Id"]).lower() or termino in str(p["Nombre"]).lower()]
            
            if encontrados:
                print(tabulate(encontrados, headers="keys", tablefmt="fancy_grid"))
            else:
                print("No se encontraron productos que coincidan con la búsqueda.")
        
        elif opcion == "3":
            print("Adiós :)")
            break
        
        else:
            print("Opción no válida, intenta de nuevo.")
