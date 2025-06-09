import os
from grupos import Grupo
from alumno import Alumno
from maestro import Maestro

class CRUDGrupo:
    def __init__(self):
        self.grupos = Grupo()
        self.alumnos = Alumno()
        self.maestros = Maestro()
        self.cargar_datos()

    def cargar_datos(self):
        try:
            if os.path.exists("grupos/grupos.json"):
                loaded = Grupo().read_json()
                if loaded and hasattr(loaded, 'items'):
                    self.grupos = loaded
        
            if os.path.exists("alumnos/alumnos.json"):
                loaded = Alumno().read_json()
                if loaded and hasattr(loaded, 'items'):
                    self.alumnos = loaded
            
            if os.path.exists("maestros/maestros.json"):
                loaded = Maestro().read_json()
                if loaded and hasattr(loaded, 'items'):
                    self.maestros = loaded
        except Exception as e:
            print(f"Error al cargar datos: {str(e)}")

    def guardar_datos(self):
        try:
            if hasattr(self.grupos, 'to_json'):
                self.grupos.to_json()
                print("Datos guardados correctamente.")
        except Exception as e:
            print(f"Error al guardar datos: {str(e)}")

    def mostrar_menu(self):
        while True:
            print("\n--- GESTIÓN DE GRUPOS ---")
            print("1. Listar grupos")
            print("2. Agregar grupo")
            print("3. Editar grupo")
            print("4. Eliminar grupo")
            print("5. Asignar maestro a grupo")
            print("6. Agregar alumno a grupo")
            print("7. Eliminar alumno de grupo")
            print("8. Guardar y salir")
            
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
                self.eliminar_alumno_grupo()
            elif opcion == "8":
                self.guardar_datos()
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida. Intente nuevamente.")

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
            
            print("\n--- LISTA DE MAESTROS ---")
            if not hasattr(self.maestros, 'items') or not self.maestros.items:
                print("No hay maestros registrados.")
                return
                
            for i, maestro in enumerate(self.maestros.items):
                print(f"{i+1}. {maestro.nombre} {maestro.apellidoPaterno} - {maestro.materia}")
                
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
            
            print("\n--- LISTA DE ALUMNOS ---")
            if not hasattr(self.alumnos, 'items') or not self.alumnos.items:
                print("No hay alumnos registrados.")
                return
                
            for i, alumno in enumerate(self.alumnos.items):
                print(f"{i+1}. {alumno.nombre} {alumno.apellidoPaterno} - {alumno.matricula}")
                
            alumno_indice = int(input("Seleccione el número del alumno a agregar: ")) - 1
            alumno = self.alumnos.items[alumno_indice]
            
            if not hasattr(grupo, 'alumnos'):
                grupo.alumnos = Alumno()
            
            grupo.alumnos.add(alumno)
            print(f"Alumno {alumno.nombre} agregado al grupo {grupo.nombre} correctamente.")
        except (IndexError, ValueError) as e:
            print(f"Selección no válida: {str(e)}")

    def eliminar_alumno_grupo(self):
        self.listar_grupos()
        if not hasattr(self.grupos, 'items') or not self.grupos.items:
            return
            
        try:
            grupo_indice = int(input("Seleccione el número del grupo: ")) - 1
            grupo = self.grupos.items[grupo_indice]
            
            if not hasattr(grupo, 'alumnos') or not grupo.alumnos or not hasattr(grupo.alumnos, 'items') or not grupo.alumnos.items:
                print("No hay alumnos en este grupo.")
                return
                
            print("\n--- ALUMNOS EN EL GRUPO ---")
            for i, alumno in enumerate(grupo.alumnos.items):
                print(f"{i+1}. {alumno.nombre} {alumno.apellidoPaterno} - {alumno.matricula}")
                
            alumno_indice = int(input("Seleccione el número del alumno a eliminar: ")) - 1
            alumno = grupo.alumnos.items[alumno_indice]
            
            confirmacion = input(f"¿Está seguro de eliminar a {alumno.nombre} del grupo? (s/n): ")
            if confirmacion.lower() == 's':
                if not grupo.alumnos.delete(indice=alumno_indice):
                    print("No se pudo eliminar el alumno del grupo.")
                else:
                    print(f"Alumno {alumno.nombre} eliminado del grupo correctamente.")
        except (IndexError, ValueError) as e:
            print(f"Selección no válida: {str(e)}")

if __name__ == "__main__":
    app = CRUDGrupo()
    app.mostrar_menu() 