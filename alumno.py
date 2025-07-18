from arreglo import Arreglo
import json
import os

class Alumno(Arreglo):
    def __init__(self, nombre=None, apellidoPaterno=None,apellidoMaterno = None, edad=None, matricula=None, email=None):
        if nombre is None and apellidoPaterno is None and apellidoMaterno is None and edad is None and matricula is None and email is None:
            Arreglo.__init__(self)
            self.isArry = True
        else:
            self.nombre = nombre
            self.apellidoPaterno = apellidoPaterno
            self.apellidoMaterno = apellidoMaterno
            self.edad = edad
            self.matricula = matricula
            self.email = email
            self.isArry = False

    def actualizar_email(self, nuevo_email):
        if not self.isArry:
            self.email = nuevo_email
            return True
        return False

    def actualizar_edad(self, nueva_edad):
        if not self.isArry:
            self.edad = nueva_edad
            return True
        return False

    def actualizar_matricula(self, nueva_matricula):
        if not self.isArry:
            self.matricula = nueva_matricula
            return True
        return False

    def mostrar_info(self):
        if self.isArry:
            for i, alumno in enumerate(self.items):
                print(f"[{i}] {alumno}")
        else:
            print(f"Nombre: {self.nombre} {self.apellidoPaterno} {self.apellidoMaterno}")
            print(f"Edad: {self.edad}")
            print(f"Matrícula: {self.matricula}")
            print(f"Email: {self.email}")

    def add(self, *items):
        if self.isArry:
            Arreglo.add(self, *items)

    def delete(self, item=None, indice=None):
        if self.isArry:
            return Arreglo.delete(self, item, indice)
        return False

    def update(self, objeto, attribute, newAttribute):
        if self.isArry:
            return Arreglo.update(self, objeto, attribute, newAttribute)
        return False

    def to_dict(self):
        if self.isArry:
            return [item.to_dict() for item in self.items] if self.items else []
        return {
            "nombre": self.nombre,
            "apellidoPaterno": self.apellidoPaterno,
            "apellidoMaterno": self.apellidoMaterno,
            "edad": self.edad,
            "matricula": self.matricula,
            "email": self.email
        }

    def to_json(self):
        carpeta = "alumnos"
        
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)
        
        json_alumno = os.path.join(carpeta, "alumnos.json")
        
        with open(json_alumno, 'w') as file:
         json.dump(self.to_dict(), file, indent=4)

    def read_json(self):
        carpeta = "alumnos"
        json_alumnos = os.path.join(carpeta, "alumnos.json")
        
        with open(json_alumnos, 'r') as file:
            data = json.load(file)
            return self._dict_to_object(data)

    def _dict_to_object(self, data):
        if not data:
            return None

        if isinstance(data, list):
            alumno_arreglo = Alumno()
            for item in data:
                alumno = Alumno(
                    item['nombre'],
                    item['apellidoPaterno'],
                    item['apellidoMaterno'],
                    item['edad'],
                    item['matricula'],
                    item['email']
                )
                alumno_arreglo.add(alumno)
            return alumno_arreglo
        else:
            alumno = Alumno(
                data['nombre'],
                data['apellidoPaterno'],
                data['apellidoMaterno'],
                data['edad'],
                data['matricula'],
                data['email']
            )
            return alumno
    
    def __str__(self):
        if self.isArry:
            return f"Alumnos (Arreglo): {len(self.items)}"
        
        return (f"Alumno: {self.nombre} {self.apellidoPaterno} {self.apellidoMaterno} - {self.matricula}")


if __name__ == "__main__":
    alumno1 = Alumno("Jose", "Guereca", "Munoz", 20, "23170046", "enrique@gmail.com")
    print(alumno1)
    alumno2 = Alumno("Iker", "Flores","Luna", 22, "23170000", "iker@gmail.com")
    print(alumno2)
    
    alumno2.actualizar_email("iker.nuevo@gmail.com")
    alumno2.actualizar_edad(23)
    alumno2.mostrar_info()

    alumnos = Alumno()
    alumnos.add(alumno1)
    alumnos.delete(indice=0)
    alumnos.add(alumno2)
    alumnos.add(Alumno("David", "Cataneda","hernandez", 18, "23170001", "david@gmail.com"))

    print(alumnos)
    
    alumnos.to_json()
   
    alumno_recuperado = Alumno().read_json()
    if alumno_recuperado.isArry:
        for a in alumno_recuperado.items:
            print(f"\nNombre: {a.nombre}")
            print(f"Apellido Paterno: {a.apellidoPaterno}")
            print(f"Apellido Materno: {a.apellidoMaterno}")
            print(f"Edad: {a.edad}")
            print(f"Matrícula: {a.matricula}")
    else:
        print(f"\nNombre: {alumno_recuperado.nombre}")
        print(f"Apellido Paterno: {alumno_recuperado.apellidoPaterno}")
        print(f"Apellido Materno: {alumno_recuperado.apellidoMaterno}")
        print(f"Edad: {alumno_recuperado.edad}")
        print(f"Matrícula: {alumno_recuperado.matricula}")
