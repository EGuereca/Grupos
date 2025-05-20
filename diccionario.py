class Diccionario:
    def __init__(self):
        self.items = {}

    def add(self, *items):
        for item in items:
            # ID
            self.items[id(item)] = item

    def delete(self, item=None, indice=None):
        try:
            if item is not None:
                del self.items[id(item)]
            elif indice is not None:
                # Convercion a lista
                keys = list(self.items.keys())
                if 0 <= indice < len(keys):
                    del self.items[keys[indice]]
            return True
        except (KeyError, IndexError):
            return False

    def update(self, objeto, attribute, newAttribute):
        if id(objeto) in self.items:
            item = self.items[id(objeto)]
            if hasattr(item, attribute):
                setattr(item, attribute, newAttribute)
                return True
        return False

    def __str__(self):
        if not self.items:
            return "No hay elementos"
        return str(len(self.items)) 