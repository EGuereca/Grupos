from arreglo import Arreglo
import json
import os
class Maestro( Arreglo):
    def __init__(self, nombre = None, apellidoPaterno = None, apellidoMaterno = None, materia = None, matricula = None):
        if nombre is None and apellidoPaterno is None and apellidoMaterno is None and materia is None and matricula is None:
            Arreglo.__init__(self)
            self.isArry = True
        else:
            self.nombre = nombre
            self.materia = materia
            self.apellidoPaterno = apellidoPaterno
            self.apellidoMaterno = apellidoMaterno
            self.matricula = matricula
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

    def to_dict(self):
        if self.isArry:
            return {
                "type": "array",
                "items": [item.to_dict() for item in self.items] if self.items else []
            }
        return {
            "nombre": self.nombre,
            "apellidoPaterno": self.apellidoPaterno,
            "apellidoMaterno": self.apellidoMaterno,
            "materia": self.materia,
            "matricula": self.matricula
        }
        
    def to_json(self):
        carpeta = "maestros"
        
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)
        
        json_maestro = os.path.join(carpeta, "maestros.json")
        
        with open(json_maestro, 'w') as file:
         json.dump(self.to_dict(), file, indent=4)
    
    def read_json(self):
        carpeta = "maestros"
        json_maestro = os.path.join(carpeta, "maestros.json")
        with open(json_maestro, 'r') as file:
            return json.load(file)
    
    def __str__(self) :
        if self.isArry:
            return f"Maestros (Arreglo): {len(self.items)}"
        
        return f"Maestro: {self.nombre} {self.apellidoPaterno} {self.apellidoMaterno} - {self.matricula}"

if __name__ == "__main__":
    maestro1 = Maestro("Antonio", "Garay","Hernandez" , "POO", "0000023")
    maestro2 = Maestro("Delia", "Tarango","Hernandez" , "Valores", "0000025")
    print(maestro1)


    print(maestro2)
    maestros = Maestro()
    maestros.add(maestro1)
    # maestros.delete(maestro1)
    maestros.add(maestro2)
    print(maestros)
    
    maestros.to_json()
    print(json.dumps(maestros.read_json(), indent=4))
    # maestro_dict = maestros.to_dict()
    # print(maestro_dict)
    
    # maestro_dict.to_json()