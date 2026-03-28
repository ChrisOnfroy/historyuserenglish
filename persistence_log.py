import os

ARCHIVO = "database.txt"

def agregar_blocker():
    """Pregunta el blocker y lo guarda en el archivo"""
    print("\n=== Create Daily Blocker  ===")
    blocker = input("¿wich is your blocker today? ")
    
    # Usar 'a' para agregar (append) sin borrar lo existente
    with open(ARCHIVO, "a") as archivo:
        archivo.write(blocker + "\n")
    
    print("¡Blocker is save!")

def ver_blockers():
    """Lee y muestra todos los blockers guardados"""
    print("\n=== All blockers ===")
    
    # Verificar si el archivo existe
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as archivo:
            # Leer todas las líneas con readlines()
            lineas = archivo.readlines()
            
            if len(lineas) == 0:
                print("dont have blockers")
            else:
                for i, linea in enumerate(lineas, 1):
                    print(f"{i}. {linea.strip()}")
    else:
        print("the file dont exist, please first create a blocker")

def main():
    isTrue = True
    """Menú principal"""
    while isTrue:
        print("\n=== MENU ===")
        print("1. create blocker")
        print("2. read blockers")
        print("3. Exit")
        
        opcion = input("Select option (1-3): ")
        
        if opcion == "1":
            agregar_blocker()
        elif opcion == "2":
            ver_blockers()
        elif opcion == "3":
            print("Program close.")
            isTrue = False
        else:
            print("invalid opcion, select again")



main()