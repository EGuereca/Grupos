import os
from alumno import Alumno
from maestro import Maestro
from grupos import Grupo

class Main:
    def __init__(self):
        self.alumnos = Alumno()
        self.maestros = Maestro()
        self.grupos = Grupo()
        
        self.cargar_datos()

    def cargar_datos(self):
        try:
            if os.path.exists("alumnos/alumnos.json"):
                loaded = Alumno().read_json()
                if loaded and hasattr(loaded, 'items'):
                    self.alumnos = loaded
            
            if os.path.exists("maestros/maestros.json"):
                loaded = Maestro().read_json()
                if loaded and hasattr(loaded, 'items'):
                    self.maestros = loaded
            
            if os.path.exists("grupos/grupos.json"):
                loaded = Grupo().read_json()
                if loaded and hasattr(loaded, 'items'):
                    self.grupos = loaded
        except Exception as e:
            print(f"Error al cargar datos: {str(e)}")

    def guardar_datos(self):
        try:
            if hasattr(self.alumnos, 'to_json'):
                self.alumnos.to_json()
            if hasattr(self.maestros, 'to_json'):
                self.maestros.to_json()
            if hasattr(self.grupos, 'to_json'):
                self.grupos.to_json()
        except Exception as e:
            print(f"Error al guardar datos: {str(e)}")

    def mostrar_menu_principal(self):
        while True:
            print("\n--- SISTEMA DE GESTIÓN ESCOLAR ---")
            print("1. Gestión de Alumnos")
            print("2. Gestión de Maestros")
            print("3. Gestión de Grupos")
            print("4. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.mostrar_menu_alumnos()
            elif opcion == "2":
                self.mostrar_menu_maestros()
            elif opcion == "3":
                self.mostrar_menu_grupos()
            elif opcion == "4":
                self.guardar_datos()
                print("¡Datos guardados correctamente!")
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida. Intente nuevamente.")

    def mostrar_menu_alumnos(self):
        while True:
            print("\n--- GESTIÓN DE ALUMNOS ---")
            print("1. Listar alumnos")
            print("2. Agregar alumno")
            print("3. Editar alumno")
            print("4. Eliminar alumno")
            print("5. Volver al menú principal")
            
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
                break
            else:
                print("Opción no válida. Intente nuevamente.")

    def mostrar_menu_maestros(self):
        while True:
            print("\n--- GESTIÓN DE MAESTROS ---")
            print("1. Listar maestros")
            print("2. Agregar maestro")
            print("3. Editar maestro")
            print("4. Eliminar maestro")
            print("5. Volver al menú principal")
            
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
                break
            else:
                print("Opción no válida. Intente nuevamente.")

    def mostrar_menu_grupos(self):
        while True:
            print("\n--- GESTIÓN DE GRUPOS ---")
            print("1. Listar grupos")
            print("2. Agregar grupo")
            print("3. Editar grupo")
            print("4. Eliminar grupo")
            print("5. Asignar maestro a grupo")
            print("6. Agregar alumno a grupo")
            print("7. Volver al menú principal")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.listar_grupos()
            elif opcion == "2":
                self.agregar_grupo()
            elif opcion == "3":
                self.editar_grupo()
            elif opcion == "4":
                self.eliminar_grupo()
            elif opcion == "5":
                self.asignar_maestro_grupo()
            elif opcion == "6":
                self.agregar_alumno_grupo()
            elif opcion == "7":
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

    def listar_grupos(self):
        print("\n--- LISTA DE GRUPOS ---")
        if not hasattr(self.grupos, 'items') or not self.grupos.items:
            print("No hay grupos registrados.")
            return
            
        for i, grupo in enumerate(self.grupos.items):
            print(f"\n{i+1}. Grupo: {grupo.nombre}")
            if grupo.maestro:
                print(f"   Maestro: {grupo.maestro.nombre} {grupo.maestro.apellidoPaterno}")
            else:
                print("   Maestro: No asignado")
            
            if hasattr(grupo, 'alumnos') and grupo.alumnos and hasattr(grupo.alumnos, 'items') and grupo.alumnos.items:
                print("   Alumnos inscritos:")
                for alumno in grupo.alumnos.items:
                    print(f"   - {alumno.nombre} {alumno.apellidoPaterno} ({alumno.matricula})")
            else:
                print("   No hay alumnos inscritos")

    def agregar_grupo(self):
        print("\n--- AGREGAR GRUPO ---")
        try:
            nombre = input("Nombre del grupo: ")
            
            nuevo_grupo = Grupo(nombre=nombre)
            
            if not hasattr(self.grupos, 'add'):
                self.grupos = Grupo() 
                self.grupos.add(nuevo_grupo)
            else:
                self.grupos.add(nuevo_grupo)
                
            print("Grupo creado correctamente.")
        except Exception as e:
            print(f"Error al crear grupo: {str(e)}")

    def editar_grupo(self):
        self.listar_grupos()
        if not hasattr(self.grupos, 'items') or not self.grupos.items:
            return
            
        try:
            indice = int(input("Seleccione el número del grupo a editar: ")) - 1
            grupo = self.grupos.items[indice]
            
            print("\n--- EDITAR GRUPO ---")
            nuevo_nombre = input(f"Nuevo nombre del grupo ({grupo.nombre}): ") or grupo.nombre
            grupo.nombre = nuevo_nombre
            print("Grupo actualizado correctamente.")
        except (IndexError, ValueError) as e:
            print(f"Selección no válida: {str(e)}")

    def eliminar_grupo(self):
        self.listar_grupos()
        if not hasattr(self.grupos, 'items') or not self.grupos.items:
            return
            
        try:
            indice = int(input("Seleccione el número del grupo a eliminar: ")) - 1
            confirmacion = input(f"¿Está seguro de eliminar el grupo {self.grupos.items[indice].nombre}? (s/n): ")
            if confirmacion.lower() == 's':
                if not self.grupos.delete(indice=indice):
                    print("No se pudo eliminar el grupo.")
                else:
                    print("Grupo eliminado correctamente.")
        except (IndexError, ValueError) as e:
            print(f"Selección no válida: {str(e)}")

    def asignar_maestro_grupo(self):
        self.listar_grupos()
        if not hasattr(self.grupos, 'items') or not self.grupos.items:
            return
            
        try:
            grupo_indice = int(input("Seleccione el número del grupo: ")) - 1
            grupo = self.grupos.items[grupo_indice]
            
            self.listar_maestros()
            if not hasattr(self.maestros, 'items') or not self.maestros.items:
                return
                
            maestro_indice = int(input("Seleccione el número del maestro a asignar: ")) - 1
            maestro = self.maestros.items[maestro_indice]
            
            grupo.maestro = maestro
            print(f"Maestro {maestro.nombre} asignado al grupo {grupo.nombre} correctamente.")
        except (IndexError, ValueError) as e:
            print(f"Selección no válida: {str(e)}")

    def agregar_alumno_grupo(self):
        self.listar_grupos()
        if not hasattr(self.grupos, 'items') or not self.grupos.items:
            return
            
        try:
            grupo_indice = int(input("Seleccione el número del grupo: ")) - 1
            grupo = self.grupos.items[grupo_indice]
            
            self.listar_alumnos()
            if not hasattr(self.alumnos, 'items') or not self.alumnos.items:
                return
                
            alumno_indice = int(input("Seleccione el número del alumno a agregar: ")) - 1
            alumno = self.alumnos.items[alumno_indice]
            
            if not hasattr(grupo, 'alumnos'):
                grupo.alumnos = Alumno()
            
            grupo.alumnos.add(alumno)
            print(f"Alumno {alumno.nombre} agregado al grupo {grupo.nombre} correctamente.")
        except (IndexError, ValueError) as e:
            print(f"Selección no válida: {str(e)}")

if __name__ == "__main__":
    app = Main()
    app.mostrar_menu_principal() 