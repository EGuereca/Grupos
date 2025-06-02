from grupos import Grupo
from alumno import Alumno

if __name__ == "__main__":
    control = True
    grupo = Grupo()
    print("Bienvenido al sistema de gestion de grupos")
    while control:
        print("1. Crear grupo")
        print("2. Agregar alumno a grupo")
        print("3. Eliminar alumno de grupo")
        print("4. Mostrar alumnos de un grupo")
        print("5. Mostrar grupos")
        print("6. Salir")
        opcion = int(input("Ingrese una opcion: "))
        
        if opcion == 1:
            nombre = input("Ingrese el nombre del grupo: ")
            maestro = input("Ingrese el nombre del maestro: ")
            grupo = Grupo(nombre, maestro)
            if  not grupo.isArry:
                print(f"Grupo {grupo.nombre} creado correctamente")
            else:
                print("Error al crear el grupo")
        elif opcion == 2:
            if not grupo.isArry:
                nombre = input("Ingrese el nombre del alumno: ")
                ap = input("Ingrese el apellido paterno del alumno: ")
                am = input("Ingrese el apellido materno del alumno: ")
                matricula = input("Ingrese la matricula del alumno: ")
                edad = int(input("Ingrese la edad del alumno: "))
                email = input("Ingrese el email de contacto del alumno: ")
                alumno = Alumno(nombre=nombre,apellidoPaterno=ap,apellidoMaterno=am,edad=edad,email=email,matricula=matricula)
                grupo.add(alumno)
                print(f"Alumno {alumno.nombre} agregado al grupo {grupo.nombre} correctamente")
            else:
                print("No hay grupos creados")
        elif opcion == 5:
            grupo_recuperado = Grupo().read_json()
            if grupo_recuperado.isArry:
                for g in grupo_recuperado.items:
                    print(f"\nNombre: {g.nombre}")
                    print(f"Maestro: {g.maestro.nombre} {g.maestro.apellidoPaterno}")
                    print("Alumnos:")
                    for alumno in g.alumnos.items:
                        print(f"- {alumno.nombre} {alumno.matricula}")
            else:
                print(f"\nNombre: {grupo_recuperado.nombre}")
                print(f"Maestro: {grupo_recuperado.maestro.nombre} {grupo_recuperado.maestro.apellidoPaterno}")
                print("Alumnos:")
                for alumno in grupo_recuperado.alumnos.items:
                    print(f"- {alumno.nombre} {alumno.matricula}")  
                    
            
        elif opcion == 6:
            control = False
