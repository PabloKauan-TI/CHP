from classes.Heap import Heap

class Floresta:
    def __init__(self, paciente):
        self.floresta = []
        self.floresta.append(Heap(paciente))
    
    def unir(self, floresta = None):
        pass

    def unir_caso1(x, y, z):
        pass

    def unir_caso2(x, y, z):
        pass

    def unir_caso3(x, y, z):
        pass

    def unir_caso4(x, y, z):
        pass

    def adicionar(self, paciente):
        self.floresta.append(Heap(paciente))
        self.floresta.sort(key= lambda heap : heap.grau)

    def atender(self):
        pass    