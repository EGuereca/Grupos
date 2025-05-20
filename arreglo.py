class Arreglo:
    def __init__(self):
        self.items = []

    def add(self, *items):
        for item in items:
            self.items.append(item)

    def delete(self, item=None, indice=None):
        try:
            if indice is not None:
                del self.items[indice]
            else:
                self.items.remove(item)
            return True
        except (IndexError, ValueError):
            return False

    def update(self, objeto, attribute, newAttribute):
        for item in self.items:
            if item == objeto:
                if hasattr(item, attribute):
                    setattr(item, attribute, newAttribute)
                    return True
        return False

    def __str__(self):
        if not self.items:
            return "No hay elementos"
        return str(len(self.items))