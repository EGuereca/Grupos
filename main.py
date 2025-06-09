from crud_alumno import CRUDAlumno
from crud_maestro import CRUDMaestro
from crud_grupo import CRUDGrupo

def mostrar_menu_principal():
    while True:
        print("\n=== SISTEMA DE GESTIÓN ESCOLAR ===")
        print("1. Gestión de Alumnos")
        print("2. Gestión de Maestros")
        print("3. Gestión de Grupos")
        print("4. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            app = CRUDAlumno()
            app.mostrar_menu()
        elif opcion == "2":
            app = CRUDMaestro()
            app.mostrar_menu()
        elif opcion == "3":
            app = CRUDGrupo()
            app.mostrar_menu()
        elif opcion == "4":
            print("\n¡Gracias por usar el sistema!")
            break
        else:
            print("\nOpción no válida. Intente nuevamente.")

if __name__ == "__main__":
    mostrar_menu_principal() 