from alumno import Alumno
from arreglo import Arreglo
from maestro import Maestro
import json
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


    def to_json(self):
        carpeta = "grupos"
        
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)
        
        json_grupos = os.path.join(carpeta, "grupos.json")
        
        with open(json_grupos, 'w') as file:
         json.dump(self.to_dict(), file, indent=4)

    def to_dict(self):
        if self.isArry:
            return  [item.to_dict() for item in self.items] if self.items else []
        return {
            "nombre": self.nombre,
            "maestro": self.maestro.to_dict() if self.maestro else None,
            "alumnos": self.alumnos.to_dict() if self.alumnos else None
        }
        
    
    def read_json(self):
        carpeta = "grupos"
        json_grupos = os.path.join(carpeta, "grupos.json")
        
        with open(json_grupos, 'r') as file:
            data = json.load(file)
            
            if isinstance(data, list):
                grupo_arreglo = Grupo()  
                for item in data:
                    grupo = self._dict_to_object(item)
                    grupo_arreglo.add(grupo)
                return grupo_arreglo
            else:
                return self._dict_to_object(data)

    def _dict_to_object(self, data):
        if not data: 
            return None

        maestro_data = data.get('maestro')
        maestro = None
        if maestro_data:
            maestro = Maestro(
                maestro_data['nombre'],
                maestro_data['apellidoPaterno'],
                maestro_data['apellidoMaterno'],
                maestro_data['materia'],
                maestro_data['matricula']
            )
        
        grupo = Grupo(data['nombre'], maestro)
        
        alumnos_data = data.get('alumnos')
        if alumnos_data and alumnos_data.get("type") == "array":
            for alumno_data in alumnos_data["items"]: 
                alumno = Alumno(
                    alumno_data['nombre'],
                    alumno_data['apellidoPaterno'],
                    alumno_data['apellidoMaterno'],
                    alumno_data['edad'],
                    alumno_data['matricula'],
                    alumno_data['email']
                )
                grupo.alumnos.add(alumno)

        
        return grupo

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
    grupo2 = Grupo("TIDSM 3", Maestro("Igmar", "Salazar","Hernandez", "POO", "00004"))

    grupo1.alumnos.add(alumno1, alumno2)
    grupo1.asignar_maestro(maestro1)

    grupos_arreglo = Grupo()
    grupos_arreglo.add(grupo1, grupo2)
    # grupos_arreglo.delete(grupo1)
    print("Usando Arreglo:", grupos_arreglo)

    grupos_arreglo.to_json()
    
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
    