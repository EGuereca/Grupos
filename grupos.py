from alumno import Alumno
from arreglo import Arreglo
from maestro import Maestro
import json
from datetime import datetime
import os

class Grupo(Arreglo):
    def __init__(self, nombre=None, maestro=None,):
        if nombre is None and maestro is None:
            Arreglo.__init__(self)
            self.isArry = True

        else:
            self.nombre = nombre
            self.maestro = maestro
            self.alumnos = Alumno()
            self.isArry = False

    def add(self, *items):
        if self.isArry:
            Arreglo.add(self, *items)
        else:
            return False

    def delete(self, item=None, indice=None):
        if self.isArry:
            return Arreglo.delete(self, item, indice)
        return False

    def update(self, objeto, attribute, newAttribute):
        if self.isArry:
            return Arreglo.update(self, objeto, attribute, newAttribute)
        return False

    def asignar_maestro(self, maestro):
        self.maestro = maestro

    def cambiarNombre(self, nombre):
        self.nombre = nombre

    def to_dict(self):
        if self.isArry:
            return  [item.to_dict() for item in self.items] if self.items else []
        return {
            "nombre": self.nombre,
            "maestro": self.maestro.to_dict() if self.maestro else None,
            "alumnos": self.alumnos.to_dict() if self.alumnos else None
        }

    def to_json(self):
        fecha = datetime.now().strftime("%Y%m%d_%H%M%S")
        carpeta = "grupos"
        
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)
        
        json_grupos = os.path.join(carpeta, f"maestros_{fecha}.json")
        
        with open(json_grupos, 'w') as file:
         json.dump(self.to_dict(), file, indent=4)

    def __str__(self):
        if self.isArry:
            return f"Grupos (Arreglo): {len(self.items)}"

        if self.maestro:
            return f"{self.nombre} {self.maestro.nombre}"
        else:
            return "Falta asignar"


if __name__ == "__main__":
    alumno1 = Alumno("Enrique", "Guereca", "Munoz", 20, "23170046", "enrique@gmail.com")
    alumno2 = Alumno("Iker", "Flores","Luna", 22, "23170000", "iker@gmail.com")
    maestro1 = Maestro("Ramiro", "Esquivel","Hernandez", "Base de Datos", "00004")
    grupo1 = Grupo("TIDSM 5", Maestro("David", "Del Toro","Hernandez", "Aplicaciones IoT", "00003"))

    grupo1.alumnos.add(alumno1, alumno2)
    grupo1.asignar_maestro(maestro1)

    print(alumno1)
    print(grupo1)

    grupos_arreglo = Grupo()
    grupos_arreglo.add(grupo1, grupo1)
    grupos_arreglo.delete(grupo1)
    print("Usando Arreglo:", grupos_arreglo)

    grupos_arreglo.to_json()

    # grupo_dict = grupos_arreglo.to_dict()
    # print(grupo_dict)