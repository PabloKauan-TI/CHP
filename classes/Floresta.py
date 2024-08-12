from classes.Heap import Heap

class Floresta:
    def __init__(self, paciente):
        self.floresta = []
        self.floresta.append(Heap(paciente))
    
    def unir(self, floresta = None):
        if floresta == None:
            a = 0
            x = a+1
            y = a+2
            while y <= (len(self.floresta)-1):
                if self.floresta[a].grau == self.floresta[x].grau and self.floresta[x].grau != self.floresta[y].grau:
                    self.unir_caso(a, x)
                a+=1
            self.unir_caso(a, x)
        else:
            for heap in floresta:
                self.floresta.append(heap)
            self.floresta.sort(key= lambda heap: heap.grau)
            self.unir()

    def unir_caso(self, x, y):
        if self.floresta[x].prioridade <= self.floresta[y].prioridade:
            self.floresta[x].filho.append(self.floresta[y])
            self.floresta[x].filho.sort(key= lambda heap : heap.grau)
            self.floresta[x].grau += 1
            self.floresta.pop(y)
        else:
            self.floresta[y].filho.append(self.floresta[x])
            self.floresta[y].filho.sort(key= lambda heap : heap.grau)
            self.floresta[y].grau += 1
            self.floresta.pop(x)
    
    def adicionar(self, paciente):
        self.floresta.append(Heap(paciente))
        self.floresta.sort(key= lambda heap : heap.grau)
        self.unir()

    def atender(self):
        pass    