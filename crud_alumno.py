import os
from alumno import Alumno

class CRUDAlumno:
    def __init__(self):
        self.alumnos = Alumno()
        self.cargar_datos()

    def cargar_datos(self):
        try:
            if os.path.exists("alumnos/alumnos.json"):
                loaded = Alumno().read_json()
                if loaded and hasattr(loaded, 'items'):
                    self.alumnos = loaded
        except Exception as e:
            print(f"Error al cargar datos: {str(e)}")

    def guardar_datos(self):
        try:
            if hasattr(self.alumnos, 'to_json'):
                self.alumnos.to_json()
                print("Datos guardados correctamente.")
        except Exception as e:
            print(f"Error al guardar datos: {str(e)}")

    def mostrar_menu(self):
        while True:
            print("\n--- GESTIÓN DE ALUMNOS ---")
            print("1. Listar alumnos")
            print("2. Agregar alumno")
            print("3. Editar alumno")
            print("4. Eliminar alumno")
            print("5. Guardar y salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.listar_alumnos()
            elif opcion == "2":
                self.agregar_alumno()
            elif opcion == "3":
                self.editar_alumno()
            elif opcion == "4":
                self.eliminar_alumno()
            elif opcion == "5":
                self.guardar_datos()
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida. Intente nuevamente.")

    def listar_alumnos(self):
        print("\n--- LISTA DE ALUMNOS ---")
        if not hasattr(self.alumnos, 'items') or not self.alumnos.items:
            print("No hay alumnos registrados.")
            return
            
        for i, alumno in enumerate(self.alumnos.items):
            print(f"{i+1}. {alumno.nombre} {alumno.apellidoPaterno} {alumno.apellidoMaterno} - {alumno.matricula}")

    def agregar_alumno(self):
        print("\n--- AGREGAR ALUMNO ---")
        try:
            nombre = input("Nombre: ")
            apellido_paterno = input("Apellido paterno: ")
            apellido_materno = input("Apellido materno: ")
            edad = int(input("Edad: "))
            matricula = input("Matrícula: ")
            email = input("Email: ")
            
            nuevo_alumno = Alumno(
                nombre=nombre, 
                apellidoPaterno=apellido_paterno, 
                apellidoMaterno=apellido_materno, 
                edad=edad, 
                matricula=matricula, 
                email=email
            )
            
            if not hasattr(self.alumnos, 'add'):
                self.alumnos = Alumno()
                self.alumnos.add(nuevo_alumno)
            else:
                self.alumnos.add(nuevo_alumno)
                
            print("Alumno agregado correctamente.")
        except ValueError as e:
            print(f"Error en los datos ingresados: {str(e)}")
        except Exception as e:
            print(f"Error al agregar alumno: {str(e)}")

    def editar_alumno(self):
        self.listar_alumnos()
        if not hasattr(self.alumnos, 'items') or not self.alumnos.items:
            return
            
        try:
            indice = int(input("Seleccione el número del alumno a editar: ")) - 1
            alumno = self.alumnos.items[indice]
            
            print("\n--- EDITAR ALUMNO ---")
            print("Deje en blanco los campos que no desea modificar")
            
            nombre = input(f"Nombre ({alumno.nombre}): ") or alumno.nombre
            apellido_paterno = input(f"Apellido paterno ({alumno.apellidoPaterno}): ") or alumno.apellidoPaterno
            apellido_materno = input(f"Apellido materno ({alumno.apellidoMaterno}): ") or alumno.apellidoMaterno
            edad = input(f"Edad ({alumno.edad}): ")
            edad = int(edad) if edad else alumno.edad
            matricula = input(f"Matrícula ({alumno.matricula}): ") or alumno.matricula
            email = input(f"Email ({alumno.email}): ") or alumno.email
            
            alumno.nombre = nombre
            alumno.apellidoPaterno = apellido_paterno
            alumno.apellidoMaterno = apellido_materno
            alumno.edad = edad
            alumno.matricula = matricula
            alumno.email = email
            
            print("Alumno actualizado correctamente.")
        except (IndexError, ValueError) as e:
            print(f"Selección no válida: {str(e)}")

    def eliminar_alumno(self):
        self.listar_alumnos()
        if not hasattr(self.alumnos, 'items') or not self.alumnos.items:
            return
            
        try:
            indice = int(input("Seleccione el número del alumno a eliminar: ")) - 1
            confirmacion = input(f"¿Está seguro de eliminar a {self.alumnos.items[indice].nombre}? (s/n): ")
            if confirmacion.lower() == 's':
                if not self.alumnos.delete(indice=indice):
                    print("No se pudo eliminar el alumno.")
                else:
                    print("Alumno eliminado correctamente.")
        except (IndexError, ValueError) as e:
            print(f"Selección no válida: {str(e)}")

if __name__ == "__main__":
    app = CRUDAlumno()
    app.mostrar_menu() 