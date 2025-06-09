import os
from maestro import Maestro

class CRUDMaestro:
    def __init__(self):
        self.maestros = Maestro()
        self.cargar_datos()

    def cargar_datos(self):
        try:
            if os.path.exists("maestros/maestros.json"):
                loaded = Maestro().read_json()
                if loaded and hasattr(loaded, 'items'):
                    self.maestros = loaded
        except Exception as e:
            print(f"Error al cargar datos: {str(e)}")

    def guardar_datos(self):
        try:
            if hasattr(self.maestros, 'to_json'):
                self.maestros.to_json()
                print("Datos guardados correctamente.")
        except Exception as e:
            print(f"Error al guardar datos: {str(e)}")

    def mostrar_menu(self):
        while True:
            print("\n--- GESTIÓN DE MAESTROS ---")
            print("1. Listar maestros")
            print("2. Agregar maestro")
            print("3. Editar maestro")
            print("4. Eliminar maestro")
            print("5. Guardar y salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.listar_maestros()
            elif opcion == "2":
                self.agregar_maestro()
            elif opcion == "3":
                self.editar_maestro()
            elif opcion == "4":
                self.eliminar_maestro()
            elif opcion == "5":
                self.guardar_datos()
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida. Intente nuevamente.")

    def listar_maestros(self):
        print("\n--- LISTA DE MAESTROS ---")
        if not hasattr(self.maestros, 'items') or not self.maestros.items:
            print("No hay maestros registrados.")
            return
            
        for i, maestro in enumerate(self.maestros.items):
            print(f"{i+1}. {maestro.nombre} {maestro.apellidoPaterno} {maestro.apellidoMaterno} - {maestro.matricula}")

    def agregar_maestro(self):
        print("\n--- AGREGAR MAESTRO ---")
        try:
            nombre = input("Nombre: ")
            apellido_paterno = input("Apellido paterno: ")
            apellido_materno = input("Apellido materno: ")
            materia = input("Materia que imparte: ")
            matricula = input("Matrícula: ")
            
            nuevo_maestro = Maestro(
                nombre=nombre, 
                apellidoPaterno=apellido_paterno, 
                apellidoMaterno=apellido_materno, 
                materia=materia, 
                matricula=matricula
            )
            
            if not hasattr(self.maestros, 'add'):
                self.maestros = Maestro()
                self.maestros.add(nuevo_maestro)
            else:
                self.maestros.add(nuevo_maestro)
                
            print("Maestro agregado correctamente.")
        except Exception as e:
            print(f"Error al agregar maestro: {str(e)}")

    def editar_maestro(self):
        self.listar_maestros()
        if not hasattr(self.maestros, 'items') or not self.maestros.items:
            return
            
        try:
            indice = int(input("Seleccione el número del maestro a editar: ")) - 1
            maestro = self.maestros.items[indice]
            
            print("\n--- EDITAR MAESTRO ---")
            print("Deje en blanco los campos que no desea modificar")
            
            nombre = input(f"Nombre ({maestro.nombre}): ") or maestro.nombre
            apellido_paterno = input(f"Apellido paterno ({maestro.apellidoPaterno}): ") or maestro.apellidoPaterno
            apellido_materno = input(f"Apellido materno ({maestro.apellidoMaterno}): ") or maestro.apellidoMaterno
            materia = input(f"Materia ({maestro.materia}): ") or maestro.materia
            matricula = input(f"Matrícula ({maestro.matricula}): ") or maestro.matricula
            
            maestro.nombre = nombre
            maestro.apellidoPaterno = apellido_paterno
            maestro.apellidoMaterno = apellido_materno
            maestro.materia = materia
            maestro.matricula = matricula
            
            print("Maestro actualizado correctamente.")
        except (IndexError, ValueError) as e:
            print(f"Selección no válida: {str(e)}")

    def eliminar_maestro(self):
        self.listar_maestros()
        if not hasattr(self.maestros, 'items') or not self.maestros.items:
            return
            
        try:
            indice = int(input("Seleccione el número del maestro a eliminar: ")) - 1
            confirmacion = input(f"¿Está seguro de eliminar a {self.maestros.items[indice].nombre}? (s/n): ")
            if confirmacion.lower() == 's':
                if not self.maestros.delete(indice=indice):
                    print("No se pudo eliminar el maestro.")
                else:
                    print("Maestro eliminado correctamente.")
        except (IndexError, ValueError) as e:
            print(f"Selección no válida: {str(e)}")

if __name__ == "__main__":
    app = CRUDMaestro()
    app.mostrar_menu() 